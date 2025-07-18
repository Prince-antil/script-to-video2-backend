from docx import Document
from tempfile import NamedTemporaryFile

def extract_text_from_docx(file_bytes: bytes) -> str:
    with NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
        tmp.write(file_bytes)
        tmp.flush()
        doc = Document(tmp.name)
        return "\n".join([para.text for para in doc.paragraphs])
