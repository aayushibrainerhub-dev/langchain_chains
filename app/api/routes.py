from fastapi import APIRouter

from app.chains.pipeline import run_resume_analysis
from app.models.request import ResumeAnalysisRequest
from app.models.response import ResumeAnalysisResponse

router = APIRouter()


@router.post("/analyze", response_model=ResumeAnalysisResponse)
def analyze_resume(payload: ResumeAnalysisRequest):
    result = run_resume_analysis(payload.resume, payload.job_description)
    return ResumeAnalysisResponse(**result)
