import os
import pandas as pd
import faiss
from sentence_transformers import SentenceTransformer

# -----------------------------
# Lazy-loaded globals
# -----------------------------
model = None
index = None
df = None


def load_resources():
    """Load model, dataset, and FAISS index if not already loaded."""
    global model, index, df

    if model is not None:
        return

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_PATH = os.path.join(BASE_DIR, "gen_ai_data.xlsx")

    # Load dataset
    df = pd.read_excel(DATA_PATH)
    df.fillna("", inplace=True)

    # Combine all text columns into one field
    df["combined_text"] = df.astype(str).agg(" ".join, axis=1)

    # Load CPU SentenceTransformer model
    model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu")

    # Compute embeddings
    embeddings = model.encode(
        df["combined_text"].tolist(),
        convert_to_numpy=True,
        batch_size=16,
        show_progress_bar=False
    )

    # Build FAISS index
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)


def recommend(query: str, top_k: int = 5):
    """Return top-k recommendations for a query string."""
    load_resources()

    query_embedding = model.encode([query], convert_to_numpy=True)
    distances, indices = index.search(query_embedding, top_k)

    results = []
    for idx in indices[0]:
        results.append({
            "text": df.iloc[idx]["combined_text"]
        })

    return results

