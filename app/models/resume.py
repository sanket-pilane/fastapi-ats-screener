from sqlalchemy import Column, Integer, String, Text, JSON
from app.db.session import Base

class ResumeAnalysis(Base):
    __tablename__ = "resume_analysis"

    id = Column(Integer, primary_key=True, index=True)
    job_description = Column(Text, nullable=False)
    resume_text = Column(Text, nullable=False)
    ats_score = Column(Integer, nullable=True)
    missing_keywords = Column(JSON, nullable=True)
    summary = Column(Text, nullable=True)
