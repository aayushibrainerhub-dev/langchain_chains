import json
import re
from typing import Dict, Any


def extract_resume_profile(resume: str) -> Dict[str, Any]:
    """Extract a simplified profile from the resume text."""
    role_match = re.search(r"(?:i am|i'm|worked as|experienced as)\s+([A-Za-z .-]+)", resume, re.IGNORECASE)
    role = role_match.group(1).strip() if role_match else "Software Engineer"

    years_match = re.search(r"(\d+)\s+years?", resume)
    years = int(years_match.group(1)) if years_match else 3

    strengths = [token.strip(" ,.") for token in re.split(r"[,;]", resume) if token.strip()]
    strengths = [s for s in strengths if len(s.split()) <= 8][:5]

    if not strengths:
        strengths = ["Problem solving", "Communication", "Teamwork"]

    return {
        "role": role,
        "years_of_experience": years,
        "strengths": strengths,
    }
