import spacy
from PyPDF2 import PdfReader

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

def parse_resume(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    doc = nlp(text)
    extracted_data = {
        "skills": [],
        "education": [],
        "experience": [],
    }

    # Basic entity extraction
    for ent in doc.ents:
        if ent.label_ in ["ORG", "GPE", "PERSON"]:
            extracted_data["experience"].append(ent.text)
        if ent.label_ in ["EDUCATION", "DATE"]:
            extracted_data["education"].append(ent.text)
        if ent.label_ in ["SKILL", "WORK_OF_ART"]:  # 'SKILL' isn't default; we’ll enhance later
            extracted_data["skills"].append(ent.text)

    return extracted_data