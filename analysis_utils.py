import re


TECH_SKILLS = [
    # Programming Languages
    "python",
    "java",
    "javascript",
    "typescript",
    "sql",
    "r",
    "scala",
    "go",
    "c++",
    "c#",
    "ruby",
    "php",
    "swift",
    "kotlin",
    "rust",
    "perl",
    "matlab",
    # Data & Analytics
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "keras",
    "spark",
    "hadoop",
    "hive",
    "kafka",
    "airflow",
    "dbt",
    "tableau",
    "power bi",
    "looker",
    # Cloud & Infrastructure
    "aws",
    "azure",
    "gcp",
    "google cloud",
    "docker",
    "kubernetes",
    "terraform",
    "jenkins",
    "ci/cd",
    "git",
    "github",
    "gitlab",
    # Databases
    "postgresql",
    "mysql",
    "mongodb",
    "redis",
    "elasticsearch",
    "snowflake",
    "redshift",
    "bigquery",
    "dynamodb",
    "cassandra",
    # Frameworks & Tools
    "react",
    "angular",
    "vue",
    "node.js",
    "django",
    "flask",
    "spring",
    "express",
    "fastapi",
    "rest api",
    "graphql",
    "microservices",
    # AI/ML
    "machine learning",
    "deep learning",
    "nlp",
    "natural language processing",
    "computer vision",
    "neural networks",
    "llm",
    "large language models",
    "gpt",
    "transformer",
    "bert",
    "openai",
    "langchain",
    # Data Engineering
    "etl",
    "data pipeline",
    "data warehouse",
    "data lake",
    "data modeling",
    "apache spark",
    "apache airflow",
    "data quality",
    "data governance",
]


def _is_missing(value):
    if value is None:
        return True
    if getattr(value, "__class__", None).__name__ == "NAType":
        return True
    try:
        return value != value
    except TypeError:
        return False


def parse_salary(salary_str):
    if _is_missing(salary_str):
        return None

    salary_str = str(salary_str)

    # If multiple salaries are concatenated, take the first complete one
    # Look for pattern: $X - $Y a year or similar
    match = re.search(r"\$([\d,]+)\s*-\s*\$([\d,]+)\s*a\s*year", salary_str)
    if match:
        low = float(match.group(1).replace(",", ""))
        high = float(match.group(2).replace(",", ""))
        return (low + high) / 2

    # Handle "From $X a year"
    match = re.search(r"from\s+\$([\d,]+)\s*a\s*year", salary_str, re.IGNORECASE)
    if match:
        return float(match.group(1).replace(",", ""))

    # Handle "Up to $X a year"
    match = re.search(r"up\s+to\s+\$([\d,]+)\s*a\s*year", salary_str, re.IGNORECASE)
    if match:
        return float(match.group(1).replace(",", ""))

    # Handle "$X a year" (single value)
    match = re.search(r"\$([\d,]+)\s*a\s*year", salary_str)
    if match:
        return float(match.group(1).replace(",", ""))

    # Handle hourly range: "$X - $Y an hour"
    match = re.search(
        r"\$([\d,]+(?:\.[\d]+)?)\s*-\s*\$([\d,]+(?:\.[\d]+)?)\s*an?\s*hour",
        salary_str,
        re.IGNORECASE,
    )
    if match:
        low = float(match.group(1).replace(",", ""))
        high = float(match.group(2).replace(",", ""))
        return ((low + high) / 2) * 2080  # Convert to annual (2080 hours/year)

    # Handle hourly: "$X an hour" or "$X/hour"
    match = re.search(
        r"\$([\d,]+(?:\.[\d]+)?)\s*(?:an?\s*hour|/hour)",
        salary_str,
        re.IGNORECASE,
    )
    if match:
        hourly = float(match.group(1).replace(",", ""))
        return hourly * 2080  # Convert to annual (2080 hours/year)

    return None


def extract_skills(description, skills=TECH_SKILLS):
    """Extract mentioned skills from job description."""
    if _is_missing(description):
        return []

    desc_lower = str(description).lower()
    found_skills = []

    for skill in skills:
        pattern = r"(?<!\w)" + re.escape(skill.lower()) + r"(?!\w)"
        if re.search(pattern, desc_lower):
            found_skills.append(skill)

    return found_skills
