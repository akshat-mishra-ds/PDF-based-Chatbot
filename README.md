# 📚 Patent FAQ Chatbot

A retrieval-based chatbot built with **Streamlit**, designed to answer questions strictly from provided **Indian Patent FAQ documents**.
It extracts Question–Answer pairs from PDFs, builds a searchable index, and retrieves the most relevant answer for user queries.

---

## 🚀 Features

* Answers strictly from `FINAL_FAQs_June_2018.pdf` and `Final_FREQUENTLY_ASKED_QUESTIONS_-PATENT.pdf`
* Uses **TF-IDF + k-Nearest Neighbors** for retrieval
* Displays **source document link** for every answer
* Maintains **chat history** within the session
* Suggests **related FAQs** when exact matches aren’t found
* Fully **open-source**, no paid API required
* Deployed on **Streamlit Community Cloud**

---

## 🛠️ Tech Stack

* **Python 3.9+**
* [Streamlit](https://streamlit.io/) – Web app framework
* [pdfplumber](https://github.com/jsvine/pdfplumber) – PDF text extraction
* [scikit-learn](https://scikit-learn.org/stable/) – TF-IDF & k-NN search
* [joblib](https://joblib.readthedocs.io/) – Model persistence

---

## 📂 Project Structure

```
pdf_based_chatbot/
├── data/                         # PDFs + processed index files
│   ├── FINAL_FAQs_June_2018.pdf
│   ├── Final_FREQUENTLY_ASKED_QUESTIONS_-PATENT.pdf
│   ├── parsed_faqs.json
│   ├── faq_vectorizer.joblib
│   ├── faq_nn.joblib
│   ├── faq_meta.json
├── utils.py                      # PDF parsing helpers
├── extract_pdfs.py               # Extracts Q&A pairs from PDFs
├── build_index.py                # Builds TF-IDF index
├── app.py                        # Streamlit chatbot app
├── requirements.txt              # Dependencies
└── README.md                     # Project documentation
```

---

## ⚙️ Setup & Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/kb_chatbot.git
   cd kb_chatbot
   ```

2. Create a virtual environment and install dependencies:

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/Mac
   .venv\Scripts\activate      # Windows

   pip install -r requirements.txt
   ```

3. Place the FAQ PDFs inside the `data/` folder.

4. Run extraction and indexing:

   ```bash
   python extract_pdfs.py
   python build_index.py
   ```

5. Launch the chatbot:

   ```bash
   streamlit run app.py
   ```

---

## 🌐 Deployment

The chatbot is deployed on **Streamlit Community Cloud**.

👉 Live Demo Link : https://pdf-based-chatbot.streamlit.app

---

## 📝 Example Query

**User:**
*When can an applicant withdraw a patent application in India?*

**Chatbot:**
Returns the exact answer from the FAQ PDF, along with:

```
Source URL: file://.../data/Final_FREQUENTLY_ASKED_QUESTIONS_-PATENT.pdf
```

---

## 🔮 Future Enhancements

* Use **semantic embeddings** (e.g., `sentence-transformers`) for better query matching
* Add **FAQ buttons** for direct selection
* Support **OCR** for scanned PDFs (Tesseract)
* Package as an **API** (FastAPI/Flask) for integration into external apps

---

## 👨‍💻 Author

Developed by **Akshat Mishra** as part of a Generative AI Evaluation Task.
---
