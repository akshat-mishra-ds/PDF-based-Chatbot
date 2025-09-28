# utils.py
import re
import os
import json
import pdfplumber

def list_pdfs(data_dir="data"):
    return [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.lower().endswith(".pdf")]

def extract_text_from_pdf(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def parse_faq_text(text, doc_name):
    """
    Extract Q&A pairs from FAQ PDFs.
    Supports 'Q.', 'Q:', 'Question:' and any line ending with '?' as a question.
    """
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    
    qas = []
    current_q = None
    current_a = []
    q_id = 0

    for line in lines:
        # Detect a question line
        if re.match(r'^(Q[.:]|Question[:.]?)\s', line, re.IGNORECASE) or line.endswith("?"):
            # If we already had a Q & A, save it
            if current_q and current_a:
                qas.append({
                    "id": f"{doc_name}_{q_id}",
                    "question": current_q,
                    "answer": " ".join(current_a).strip(),
                    "doc": doc_name
                })
                q_id += 1
                current_a = []
            # Start new question
            current_q = re.sub(r'^(Q[.:]|Question[:.]?)\s*', '', line, flags=re.IGNORECASE).strip()
        else:
            # Treat as part of answer
            if current_q:
                current_a.append(line)

    # Save last pair
    if current_q and current_a:
        qas.append({
            "id": f"{doc_name}_{q_id}",
            "question": current_q,
            "answer": " ".join(current_a).strip(),
            "doc": doc_name
        })

    return qas

def save_json(obj, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
