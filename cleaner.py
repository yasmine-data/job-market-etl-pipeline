import re


# Master skill taxonomy to parse from descriptions
TARGET_SKILLS = [
    "Python",
    "SQL",
    "Excel",
    "Power BI",
    "Tableau",
    "Pandas",
    "Snowflake",
    "AWS",
    "Docker"
]


def extract_skills(description):
    """Scans job description text and extracts matching technical skills."""
    found_skills = []

    for skill in TARGET_SKILLS:
        # Match exact words inside the text
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, description, re.IGNORECASE):
            found_skills.append(skill)

    return found_skills


def parse_job_record(raw_job):
    """Transforms a raw job record into a structured, skill-enriched payload."""
    description = raw_job.get("description", "")
    extracted_skills = extract_skills(description)

    cleaned_record = {
        "id": raw_job.get("id"),
        "title": raw_job.get("title"),
        "company": raw_job.get("company"),
        "location": raw_job.get("location"),
        "skills": extracted_skills
    }

    return cleaned_record


if __name__ == "__main__":
    print("Testing cleaner module...")
    sample_raw_job = {
        "id": "job_101",
        "title": "Junior Data Analyst",
        "company": "Apex Analytics",
        "location": "Remote",
        "description": "Looking for an entry-level analyst comfortable with Python, SQL, and Excel for weekly client reporting."
    }

    processed = parse_job_record(sample_raw_job)
    print("Processed Record:")
    print(processed)
