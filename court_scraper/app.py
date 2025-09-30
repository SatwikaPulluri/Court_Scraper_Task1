from flask import Flask, render_template, request, send_file
from scraper import fetch_highcourt_case, fetch_districtcourt_case
from database import insert_case, get_connection
from fpdf import FPDF
from datetime import datetime, timedelta

app = Flask(__name__)

# Inject tomorrow's date into all templates
@app.context_processor
def inject_current_date():
    tomorrow = datetime.today() + timedelta(days=1)
    return {'current_date': tomorrow.strftime('%d-%m-%Y')}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search', methods=['POST'])
def search():
    case_type = request.form['case_type']
    case_number = request.form['case_number']
    year = request.form['year']
    court_type = request.form['court_type']

    if court_type == "highcourt":
        case_data = fetch_highcourt_case(case_type, case_number, year)
    else:
        case_data = fetch_districtcourt_case(case_type, case_number, year)

    # Save to MySQL
    insert_case(case_data)

    return render_template("result.html", case=case_data)

@app.route('/download', methods=['POST'])
def download_pdf():
    case_type = request.form['case_type']
    case_number = request.form['case_number']
    year = request.form['year']
    parties = request.form['parties']
    status = request.form['status']
    next_hearing = request.form['next_hearing']

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Court Case Report", ln=1, align='C')
    pdf.cell(200, 10, txt=f"Case: {case_type} {case_number}/{year}", ln=1)
    pdf.cell(200, 10, txt=f"Parties: {parties}", ln=1)
    pdf.cell(200, 10, txt=f"Status: {status}", ln=1)
    pdf.cell(200, 10, txt=f"Next Hearing: {next_hearing}", ln=1)

    filename = f"case_{case_number}.pdf"
    pdf.output(filename)

    return send_file(filename, as_attachment=True)

@app.route('/history')
def history():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM cases ORDER BY id DESC")
    cases = cursor.fetchall()
    conn.close()
    return render_template("history.html", cases=cases)

if __name__ == '__main__':
    app.run(debug=True)
