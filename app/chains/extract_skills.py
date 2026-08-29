import re
from typing import List


def extract_skills(text: str) -> List[str]:
    """Extract a simple set of skills from free-form text."""
    tokens = re.findall(r"[A-Za-z#+.]+", text)
    skill_words = [token.strip(" ,.;:-") for token in tokens if len(token) > 2]

    preferred = [
        "python",
        "fastapi",
        "langchain",
        "api",
        "docker",
        "machine learning",
        "rest",
        "vector",
        "database",
        "backend",
        "sql",
        "aws",
        "kubernetes",
    ]

    extracted = []
    lowered = [word.lower() for word in skill_words]
    for skill in preferred:
        if skill in " ".join(lowered):
            extracted.append(skill)

    if not extracted:
        extracted = [word.lower() for word in skill_words[:5]]

    return extracted
