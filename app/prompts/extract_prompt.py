EXTRACT_PROMPT = """
You are an expert resume parser.
Extract the candidate's professional role, years of experience, and key strengths from the resume.
Return a JSON object with keys: role, years_of_experience, strengths.
Resume:
{resume}
"""
