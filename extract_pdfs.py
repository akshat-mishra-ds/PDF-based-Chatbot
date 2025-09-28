# extract_pdfs.py
import os
from utils import list_pdfs, extract_text_from_pdf, parse_faq_text, save_json

DATA_DIR = "data"
OUT_FILE = os.path.join(DATA_DIR, "parsed_faqs.json")

def main():
    pdfs = list_pdfs(DATA_DIR)
    all_qas = []
    for pdf in pdfs:
        print(f"Parsing {pdf}...")
        raw_text = extract_text_from_pdf(pdf)
        qas = parse_faq_text(raw_text, os.path.basename(pdf))
        all_qas.extend(qas)
    print(f"Extracted {len(all_qas)} Q&A pairs.")
    save_json(all_qas, OUT_FILE)
    print("Saved parsed Q&A to", OUT_FILE)

if __name__ == "__main__":
    main()
