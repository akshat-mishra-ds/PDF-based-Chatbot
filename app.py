# app.py
import streamlit as st
import joblib
import os
import json

DATA_DIR = "data"
VECTORIZER_PATH = os.path.join(DATA_DIR, "faq_vectorizer.joblib")
NN_PATH = os.path.join(DATA_DIR, "faq_nn.joblib")
META_PATH = os.path.join(DATA_DIR, "faq_meta.json")

# Load index and metadata
@st.cache_resource
def load_index():
    vect = joblib.load(VECTORIZER_PATH)
    nn = joblib.load(NN_PATH)
    with open(META_PATH, "r", encoding="utf-8") as f:
        meta = json.load(f)
    return vect, nn, meta

vect, nn, meta = load_index()

st.set_page_config(page_title="Patent FAQ Chatbot", layout="wide")
st.title("Patent FAQ Chatbot")
st.write("Answers are strictly from the provided FAQ documents.")

if "history" not in st.session_state:
    st.session_state.history = []

query = st.text_input("Ask a question:", key="query")
threshold = st.sidebar.slider("Similarity threshold", 0.0, 1.0, 0.3, 0.01)

def search_faqs(q, top_k=3):
    q_vec = vect.transform([q])
    # 🔹 Prevent error when fewer QAs than neighbors requested
    top_k = min(top_k, len(meta))
    distances, idxs = nn.kneighbors(q_vec, n_neighbors=top_k)
    sims = 1 - distances[0]
    results = []
    for sim, idx in zip(sims, idxs[0]):
        item = meta[idx]
        results.append({
            "sim": float(sim),
            "question": item["question"],
            "answer": item["answer"],
            "doc": item["doc"]
        })
    return results

if st.button("Ask"):
    if not query.strip():
        st.warning("Please type a question.")
    else:
        results = search_faqs(query)
        if not results:
            st.error("No FAQs available in the knowledge base.")
        else:
            top = results[0]
            if top["sim"] < threshold:
                st.error("I cannot find an answer for that. Try one of these questions:")
                for r in results:
                    st.write(f"- {r['question']} (from {r['doc']})")
                st.session_state.history.append({"user": query, "bot": "No answer found."})
            else:
                answer = top["answer"]
                st.markdown(f"**Answer:** {answer}")
                st.markdown(f"**Source URL:** file://{os.path.abspath(os.path.join(DATA_DIR, top['doc']))}")
                st.session_state.history.append({"user": query, "bot": answer})

st.markdown("---")
st.subheader("Conversation History")
for turn in st.session_state.history[::-1]:
    st.write(f"**You:** {turn['user']}")
    st.write(f"**Bot:** {turn['bot']}")
