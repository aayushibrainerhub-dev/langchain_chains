def score_resume(profile: dict, matched_skills: list, job_description: str) -> float:
    """Score the resume against the job description using a simple heuristic."""
    score = 0.0
    if profile.get("role"):
        score += 20
    score += min(40, len(matched_skills) * 10)
    if "backend" in job_description.lower() or "engineer" in job_description.lower():
        score += 20
    if profile.get("years_of_experience", 0) >= 3:
        score += 20
    return round(min(100.0, score), 2)
