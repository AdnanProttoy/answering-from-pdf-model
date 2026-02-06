# pdf_loader.py
from pypdf import PdfReader  # using pypdf instead of PyPDF2

def load_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"  # keep line breaks between pages
    return text
