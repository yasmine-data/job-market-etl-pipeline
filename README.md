# Job Matching Pipeline

A simple Python-based pipeline that scrapes job postings, cleans and extracts required skills, and matches candidates based on skill set overlap.

## Structure

1. `scraper.py` - Retrieves raw job listings.
2. `cleaner.py` - Parses descriptions and extracts required technical skills.
3. `matcher.py` - Calculates percentage match scores for candidate skill sets.
4. `pipeline.py` - Runs the end-to-end process and outputs candidate evaluation results.

## Usage

Run the main pipeline:

```bash
python pipeline.py
