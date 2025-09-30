import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",          # change if needed
        password="Satwika@21",  # replace with your MySQL password
        database="court_scraper"
    )

def insert_case(case_data):
    conn = get_connection()
    cursor = conn.cursor()
    sql = """INSERT INTO cases 
             (case_type, case_number, year, parties, filing_date, next_hearing, status, cause_listed, raw_html)
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    values = (
        case_data['case_type'], case_data['case_number'], case_data['year'],
        case_data['parties'], case_data['filing_date'], case_data['next_hearing'],
        case_data['status'], case_data['cause_listed'], case_data['raw_html']
    )
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
