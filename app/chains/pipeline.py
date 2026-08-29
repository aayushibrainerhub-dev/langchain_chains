from concurrent.futures import ThreadPoolExecutor
from typing import Any, Dict, List, Tuple

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda

from app.chains.branch import runnable_branch
from app.chains.extract_resume import extract_resume_profile
from app.chains.extract_skills import extract_skills
from app.chains.match_jd import match_job_description
from app.chains.score_resume import score_resume
from app.chains.suggestion import generate_suggestions
from app.config import GROK_API_CLOUD_KEY
from app.prompts.extract_prompt import EXTRACT_PROMPT
from app.prompts.match_prompt import MATCH_PROMPT
from app.prompts.score_prompt import SCORE_PROMPT
from app.prompts.suggestion_prompt import SUGGESTION_PROMPT

def _llm_available() -> bool:
    return bool(GROK_API_CLOUD_KEY)

def _build_lcel_chain():
    extract_prompt = PromptTemplate.from_template(EXTRACT_PROMPT)
    match_prompt = PromptTemplate.from_template(MATCH_PROMPT)
    score_prompt = PromptTemplate.from_template(SCORE_PROMPT)
    suggestion_prompt = PromptTemplate.from_template(SUGGESTION_PROMPT)

    return (
        RunnableLambda(lambda x: x)
        | RunnableLambda(lambda x: {"resume": x["resume"], "job_description": x["job_description"]})
        | extract_prompt
        | RunnableLambda(lambda x: x)
    )

def _parallel_extract_profile_and_skills(resume: str, job_description: str) -> Tuple[Dict[str, Any], List[str]]:
    with ThreadPoolExecutor(max_workers=2) as executor:
        profile_future = executor.submit(extract_resume_profile, resume)
        skills_future = executor.submit(extract_skills, resume + " " + job_description)
        return profile_future.result(), skills_future.result()


def _parallel_score_and_suggestions(
    profile: Dict[str, Any],
    matched_skills: List[str],
    job_description: str,
    missing_skills: List[str],
) -> Tuple[float, List[str]]:
    with ThreadPoolExecutor(max_workers=2) as executor:
        score_future = executor.submit(score_resume, profile, matched_skills, job_description)
        suggestions_future = executor.submit(generate_suggestions, profile, matched_skills, missing_skills)
        return score_future.result(), suggestions_future.result()


def _run_parallel_pipeline(resume: str, job_description: str, branch_name: str) -> Dict[str, Any]:
    profile, skills = _parallel_extract_profile_and_skills(resume, job_description)
    matched_skills = match_job_description(skills, job_description)
    missing_skills = [skill for skill in skills if skill not in matched_skills]
    score, suggestions = _parallel_score_and_suggestions(profile, matched_skills, job_description, missing_skills)

    return {
        "extracted_profile": profile,
        "skills": skills,
        "matched_skills": matched_skills,
        "score": score,
        "suggestions": suggestions,
        "branch": branch_name,
        "chain_type": "parallel",
    }

def run_resume_analysis(resume: str, job_description: str) -> Dict[str, Any]:
    """Run the resume analysis pipeline using parallel chaining and branching logic."""
    branch = runnable_branch(_llm_available)
    branch_name = branch["branch"]

    return _run_parallel_pipeline(resume, job_description, branch_name=branch_name)
