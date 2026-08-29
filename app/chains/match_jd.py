from typing import List, Set


def match_job_description(skills: List[str], job_description: str) -> List[str]:
    """Return the skills that are relevant to the job description."""
    text = job_description.lower()
    matched = []
    for skill in skills:
        if skill.lower() in text:
            matched.append(skill)
    if not matched:
        matched = skills[:3]
    return matched
