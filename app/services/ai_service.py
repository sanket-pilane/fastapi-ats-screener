import google.generativeai as genai
from app.core.config import settings
from app.schemas.resume import AnalysisResult
import json

genai.configure(api_key=settings.GEMINI_API_KEY)

class AIService:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-2.5-flash')

    async def analyze_resume(self, job_description: str, resume_text: str) -> AnalysisResult:
        prompt = f"""
        You are an expert ATS (Applicant Tracking System) scanner.
        Analyze the following resume against the job description.

        Job Description:
        {job_description}

        Resume:
        {resume_text}

        Provide the output in the following JSON format:
        {{
            "ats_score": <integer between 0 and 100>,
            "missing_keywords": [<list of 5 missing keywords>],
            "summary": "<2 sentence summary of the resume's fit>"
        }}
        """
        
        try:
            response = self.model.generate_content(prompt)
            # Clean up the response to ensure it's valid JSON
            text = response.text.replace('```json', '').replace('```', '').strip()
            data = json.loads(text)
            return AnalysisResult(**data)
        except Exception as e:
            # Fallback or error handling
            print(f"Error in AI analysis: {e}")
            return AnalysisResult(ats_score=0, missing_keywords=["Error analyzing"], summary="Failed to analyze resume.")

ai_service = AIService()
