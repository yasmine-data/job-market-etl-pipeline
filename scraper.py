import json
import requests
from bs4 import BeautifulSoup


def fetch_job_listings(query="Data Analyst", location="Remote"):
    # TODO: replace mock payload with live Requests endpoint once API key is configured
    print(f"Fetching job listings for '{query}' in '{location}'...")

    jobs = [
        {
            "id": "job_101",
            "title": "Junior Data Analyst",
            "company": "Apex Analytics",
            "location": "Remote",
            "description": "Looking for a entry-level analyst comfortable with Python, SQL, and Excel for weekly client reporting."
        },
        {
            "id": "job_102",
            "title": "BI & Data Analyst",
            "company": "Vanguard Media",
            "location": "Remote",
            "description": "Need an analyst to build dynamic executive dashboards using Power BI, SQL, and Tableau."
        },
        {
            "id": "job_103",
            "title": "Data Analyst (ETL Focus)",
            "company": "Logistics Direct",
            "location": "Remote",
            "description": "Requires experience in Python, Pandas, SQL, and Snowflake for daily pipeline validation."
        }
    ]

    return jobs


if __name__ == "__main__":
    print("Testing scraper module...")
    data = fetch_job_listings()
    print(f"Ingested {len(data)} raw job records.")

    # Quick sanity check on payload structure
    print(json.dumps(data[0], indent=2))
