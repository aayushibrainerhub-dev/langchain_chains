from typing import List


def generate_suggestions(profile: dict, matched_skills: List[str], missing_skills: List[str]) -> List[str]:
    """Generate practical suggestions based on the gap between the candidate and the job."""
    suggestions = []
    if "langchain" not in matched_skills:
        suggestions.append("Add LangChain projects to your portfolio to strengthen your backend profile.")
    if "fastapi" not in matched_skills:
        suggestions.append("Build a FastAPI service and document it publicly to demonstrate API skills.")
    if missing_skills:
        suggestions.append(f"Focus on improving expertise in: {', '.join(missing_skills[:3])}")
    if not suggestions:
        suggestions.append("Continue refining your experience and adding measurable project outcomes.")
    return suggestions[:3]
