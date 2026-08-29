from app.chains.pipeline import run_resume_analysis


def test_run_resume_analysis_returns_expected_sections():
    resume = """
    I am a Python developer with 4 years of experience in FastAPI, Docker, and machine learning.
    I have built REST APIs and worked with LangChain and vector databases.
    """
    job_description = """
    We are hiring a Python backend engineer with FastAPI, LangChain, and API development experience.
    """

    result = run_resume_analysis(resume=resume, job_description=job_description)

    assert result["extracted_profile"]["role"]
    assert result["skills"]
    assert result["matched_skills"]
    assert result["score"] >= 0
    assert result["suggestions"]
    assert result["branch"] in {"llm", "fallback"}
    assert result["chain_type"] == "parallel"
