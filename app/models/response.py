from typing import Any, Dict, List

from pydantic import BaseModel, Field


class ResumeAnalysisResponse(BaseModel):
    extracted_profile: Dict[str, Any] = Field(default_factory=dict)
    skills: List[str] = Field(default_factory=list)
    matched_skills: List[str] = Field(default_factory=list)
    score: float = Field(default=0.0)
    suggestions: List[str] = Field(default_factory=list)
