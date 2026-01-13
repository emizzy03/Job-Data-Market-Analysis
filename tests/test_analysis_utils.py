from analysis_utils import TECH_SKILLS, extract_skills, parse_salary


def test_parse_salary_annual_range():
    assert parse_salary("$100,000 - $120,000 a year") == 110000


def test_parse_salary_hourly_range():
    assert parse_salary("$40 - $60 an hour") == 104000


def test_parse_salary_hourly_slash_format():
    assert parse_salary("$55/hour") == 114400


def test_extract_skills_with_non_word_chars():
    description = "Looking for engineers with C++ and C# experience plus SQL."
    skills = extract_skills(description, skills=TECH_SKILLS)
    assert "c++" in skills
    assert "c#" in skills
    assert "sql" in skills
