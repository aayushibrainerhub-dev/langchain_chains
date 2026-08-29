from pydantic import BaseModel, Field


class ResumeAnalysisRequest(BaseModel):
    resume: str = Field(..., min_length=10)
    job_description: str = Field(..., min_length=10)
