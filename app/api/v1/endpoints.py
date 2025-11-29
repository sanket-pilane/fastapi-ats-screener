from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.resume import ResumeAnalysis
from app.schemas.resume import ResumeInput, ResumeResponse, AnalysisResult
from app.services.ai_service import ai_service

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok"}

@router.post("/score", response_model=ResumeResponse)
async def score_resume(input_data: ResumeInput, db: Session = Depends(get_db)):
    # Perform analysis
    analysis_result = await ai_service.analyze_resume(input_data.job_description, input_data.candidate_resume)
    
    # Store in DB
    db_analysis = ResumeAnalysis(
        job_description=input_data.job_description,
        resume_text=input_data.candidate_resume,
        ats_score=analysis_result.ats_score,
        missing_keywords=analysis_result.missing_keywords,
        summary=analysis_result.summary
    )
    db.add(db_analysis)
    db.commit()
    db.refresh(db_analysis)
    
    return ResumeResponse(score_id=db_analysis.id, message="Analysis completed successfully")

@router.get("/feedback/{score_id}", response_model=AnalysisResult)
def get_feedback(score_id: int, db: Session = Depends(get_db)):
    analysis = db.query(ResumeAnalysis).filter(ResumeAnalysis.id == score_id).first()
    if not analysis:
        raise HTTPException(status_code=404, detail="Analysis not found")
    
    return AnalysisResult(
        ats_score=analysis.ats_score,
        missing_keywords=analysis.missing_keywords,
        summary=analysis.summary
    )
