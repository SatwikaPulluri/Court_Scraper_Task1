def fetch_highcourt_case(case_type, case_number, year):
    # Simulated data (replace with Selenium if needed)
    return {
        "case_type": case_type,
        "case_number": case_number,
        "year": year,
        "parties": "Petitioner A vs Respondent B",
        "filing_date": "01-01-2020",
        "next_hearing": "02-10-2025",
        "status": "Pending",
        "cause_listed": 1,  # Simulated: case listed
        "raw_html": "<html>sample response</html>"
    }

def fetch_districtcourt_case(case_type, case_number, year):
    return {
        "case_type": case_type,
        "case_number": case_number,
        "year": year,
        "parties": "X vs Y",
        "filing_date": "15-08-2021",
        "next_hearing": "05-10-2025",
        "status": "Disposed",
        "cause_listed": 0,  # Simulated: not listed
        "raw_html": "<html>sample response</html>"
    }
