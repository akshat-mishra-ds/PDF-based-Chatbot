# build_index.py
import json
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import joblib

DATA_DIR = "data"
FAQS_FILE = os.path.join(DATA_DIR, "parsed_faqs.json")
VECTORIZER_PATH = os.path.join(DATA_DIR, "faq_vectorizer.joblib")
NN_PATH = os.path.join(DATA_DIR, "faq_nn.joblib")
META_PATH = os.path.join(DATA_DIR, "faq_meta.json")

def main():
    with open(FAQS_FILE, "r", encoding="utf-8") as f:
        qas = json.load(f)
    questions = [q["question"] for q in qas]
    
    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform(questions)
    
    nn = NearestNeighbors(n_neighbors=5, metric="cosine")
    nn.fit(X)
    
    joblib.dump(vectorizer, VECTORIZER_PATH)
    joblib.dump(nn, NN_PATH)
    
    with open(META_PATH, "w", encoding="utf-8") as f:
        json.dump(qas, f, ensure_ascii=False, indent=2)
    
    print("Index built successfully.")

if __name__ == "__main__":
    main()
