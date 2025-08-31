import fitz  # PyMuPDF
from docx import Document

def parse_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def parse_docx(file_path):
    doc = Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

def parse_file(file):
    # file is a Streamlit UploadedFile
    if file.type == "application/pdf":
        with open("temp.pdf", "wb") as f:
            f.write(file.read())
        return parse_pdf("temp.pdf")
    elif file.type in ["application/vnd.openxmlformats-officedocument.wordprocessingml.document", "application/msword"]:
        with open("temp.docx", "wb") as f:
            f.write(file.read())
        return parse_docx("temp.docx")
    else:
        return file.getvalue().decode("utf-8")
