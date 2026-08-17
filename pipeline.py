import json
from scraper import fetch_job_listings
from cleaner import parse_job_record
from matcher import evaluate_job_candidate


def run_pipeline(candidate_profile, query="Data Analyst", location="Remote"):
    """Orchestrates the full ETL and job-matching pipeline."""
    print("==================================================")
    print("          JOB MATCHING PIPELINE STARTED           ")
    print("==================================================\n")

    # Step 1: Ingestion / Scraping
    print(f"[1/3] Fetching raw job postings for '{query}'...")
    raw_jobs = fetch_job_listings(query=query, location=location)
    print(f"      -> Retrieved {len(raw_jobs)} job records.\n")

    # Step 2: Extraction & Cleaning
    print("[2/3] Extracting required technical skills...")
    cleaned_jobs = [parse_job_record(job) for job in raw_jobs]
    print(f"      -> Successfully processed {len(cleaned_jobs)} records.\n")

    # Step 3: Scoring & Candidate Matching
    print(f"[3/3] Evaluating candidate matches for: {candidate_profile.get('name')}...")
    evaluations = []
    for job in cleaned_jobs:
        match_result = evaluate_job_candidate(job, candidate_profile)
        evaluations.append(match_result)

    print("      -> Pipeline processing completed successfully!\n")
    print("==================================================")
    print("               PIPELINE RESULTS SUMMARY           ")
    print("==================================================\n")

    return evaluations


if __name__ == "__main__":
    # Define candidate profile for testing
    my_profile = {
        "name": "Yasmin",
        "skills": ["Python", "SQL", "Excel", "AWS", "Docker"]
    }

    results = run_pipeline(candidate_profile=my_profile)
    print(json.dumps(results, indent=2))
