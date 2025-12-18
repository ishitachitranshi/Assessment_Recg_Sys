from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from recommender import recommend

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
# Health check
# -----------------------------
@app.get("/")
def health():
    return {"status": "running"}

# -----------------------------
# Search endpoint
# -----------------------------
@app.post("/search")
def search(query: str = Form(...)):
    results = recommend(query, top_k=5)
    return {"results": results}

