def calculate_match_score(candidate_skills, required_skills):
    """Calculates percentage match between candidate skills and job requirements."""
    if not required_skills:
        return 100.0  # Default to full match if no specific skills are required

    candidate_set = set(skill.lower() for skill in candidate_skills)
    required_set = set(skill.lower() for skill in required_skills)

    matched_skills = candidate_set.intersection(required_set)
    match_percentage = (len(matched_skills) / len(required_set)) * 100

    return round(match_percentage, 1)


def evaluate_job_candidate(job_record, candidate_profile):
    """Evaluates a single cleaned job record against a candidate profile."""
    required_skills = job_record.get("skills", [])
    candidate_skills = candidate_profile.get("skills", [])

    score = calculate_match_score(candidate_skills, required_skills)

    matched_skills = list(
        set(candidate_skills).intersection(set(required_skills))
    )
    missing_skills = list(
        set(required_skills) - set(candidate_skills)
    )

    return {
        "job_id": job_record.get("id"),
        "title": job_record.get("title"),
        "company": job_record.get("company"),
        "match_score": score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }


if __name__ == "__main__":
    print("Testing matcher module...")
    sample_job = {
        "id": "job_101",
        "title": "Junior Data Analyst",
        "company": "Apex Analytics",
        "skills": ["Python", "SQL", "Excel"]
    }

    sample_candidate = {
        "name": "Yasmin",
        "skills": ["Python", "SQL", "AWS", "Docker"]
    }

    evaluation = evaluate_job_candidate(sample_job, sample_candidate)
    print("Candidate Evaluation Result:")
    print(evaluation)
