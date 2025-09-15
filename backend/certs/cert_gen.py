from fpdf import FPDF
import json

def generate_cert(data, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Certificate", ln=True, align='C')
    pdf.output(filename)
    with open(filename.replace('.pdf', '.json'), 'w') as f:
        json.dump(data, f)
        