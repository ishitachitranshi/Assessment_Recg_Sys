from sentence_transformers import SentenceTransformer
import faiss
import pandas as pd
import numpy as np

df = pd.read_csv("data/shl_products.csv")

model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(df["description"].tolist())

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

def recommend(query, top_k=5):
    q_emb = model.encode([query])
    D, I = index.search(np.array(q_emb), top_k)

    return df.iloc[I[0]].to_dict(orient="records")

