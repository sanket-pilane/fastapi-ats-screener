from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import MagicMock, patch
from app.services.ai_service import ai_service
from app.schemas.resume import AnalysisResult

client = TestClient(app)

def test_health_check():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

@patch("app.services.ai_service.ai_service.analyze_resume")
def test_score_resume(mock_analyze):
    mock_analyze.return_value = AnalysisResult(
        ats_score=85,
        missing_keywords=["Python", "FastAPI"],
        summary="Good fit."
    )
    
    response = client.post(
        "/api/v1/score",
        json={
            "job_description": "Python Developer",
            "candidate_resume": "I know Python."
        }
    )
    assert response.status_code == 200
    assert "score_id" in response.json()

def test_get_feedback_not_found():
    response = client.get("/api/v1/feedback/99999")
    assert response.status_code == 404
