from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -----------------------------
# App initialization
# -----------------------------
app = FastAPI(title="SHL Assessment Recommendation API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Load and prepare data ONCE
# -----------------------------
df = pd.read_excel("gen_ai_data.xlsx")
df.fillna("", inplace=True)

df["combined_text"] = (
    df["Product Name"] + " " +
    df["Description"] + " " +
    df["Assessment Type"]
)

vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(df["combined_text"])

# -----------------------------
# Recommendation logic
# -----------------------------
def recommend(query: str, top_k: int = 5):
    query_vec = vectorizer.transform([query])
    scores = cosine_similarity(query_vec, tfidf_matrix)[0]

    top_indices = scores.argsort()[::-1][:top_k]

    results = []
    for idx in top_indices:
        results.append({
            "title": df.iloc[idx]["Product Name"],
            "description": df.iloc[idx]["Description"],
            "score": round(float(scores[idx]), 3)
        })
    return results

# -----------------------------
# Health check (IMPORTANT for Render)
# -----------------------------
@app.get("/")
def health():
    return {"status": "running"}

# -----------------------------
# Search endpoint
# -----------------------------
@app.post("/search")
def search(query: str = Form(...)):
    return recommend(query)

