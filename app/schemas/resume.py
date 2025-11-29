from pydantic import BaseModel
from typing import List, Optional

class ResumeInput(BaseModel):
    job_description: str
    candidate_resume: str

class AnalysisResult(BaseModel):
    ats_score: int
    missing_keywords: List[str]
    summary: str

class ResumeResponse(BaseModel):
    score_id: int
    message: str = "Analysis queued/completed"
