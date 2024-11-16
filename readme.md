# Job Scraper for LinkedIn

This project is a Python script that uses Selenium to scrape job listings from LinkedIn based on a search query and location. The script extracts job titles, company names, locations, and links to job postings and saves the results.

---

## Features

- **Automated Job Search**: Scrapes LinkedIn job listings for a specific query and location.
- **Detailed Results**: Extracts job title, company name, location, and link to the job posting.
- **Headless Browsing**: Runs in headless mode to ensure efficiency and avoid opening browser windows.

---

## Requirements

- Python 3.9+
- Google Chrome
- ChromeDriver

---

## Installation

### 1. Clone the repository:

```bash
git clone https://github.com/Camilo0808/Linkedin-Scraper
cd Linkedin-Scraper
```

### 2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

### Run the Script:

```bash
python job_scraper.py
```

### Enter Search Parameters:

- **Job Title or Keyword**: Enter the job title or keyword (e.g., `Data Scientist`).
- **Location**: Specify the location (e.g., `San Francisco`).
- **Maximum Jobs**: Enter the maximum number of jobs to retrieve.

### Output:

- Displays the scraped job listings in the terminal.
- Saves the results to a `job_listings.csv` file:

```csv
title,company,location,link
"Data Scientist","Google","San Francisco, CA","https://linkedin.com/job/..."
...
```

---

## Notes

- Ensure you have Google Chrome installed on your system.
- The script uses `webdriver-manager` to automatically manage ChromeDriver versions.
- Use responsibly to avoid LinkedIn's anti-scraping mechanisms.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.