<<<<<<< HEAD
from PyPDF2 import PdfReader
=======
from pypdf import PdfReader
>>>>>>> 546c7af (Add .gitignore and remove venv)

def load_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
<<<<<<< HEAD
        text += page.extract_text() + "\n"
=======
        text += page.extract_text()
>>>>>>> 546c7af (Add .gitignore and remove venv)
    return text
