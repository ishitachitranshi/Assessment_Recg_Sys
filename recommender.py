import os
import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "gen_ai_data.xlsx")

# Load Excel dataset
df = pd.read_excel(DATA_PATH)
df.fillna("", inplace=True)

# Combine text fields (important for RAG quality)
df["combined_text"] = df.astype(str).agg(" ".join, axis=1)

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create embeddings
embeddings = model.encode(
    df["combined_text"].tolist(),
    convert_to_numpy=True,
    show_progress_bar=False
)

# FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

def recommend(query: str, top_k: int = 5):
    query_embedding = model.encode([query], convert_to_numpy=True)
    _, indices = index.search(query_embedding, top_k)

    results = []
    for i in indices[0]:
        results.append({
            "text": df.iloc[i]["combined_text"]
        })

    return results

