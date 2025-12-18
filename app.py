from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from recommender import recommend

app = FastAPI(title="SHL Assessment Recommendation API")

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check for Render
@app.get("/")
def health():
    return {"status": "running"}

# Search endpoint
@app.post("/search")
def search(query: str = Form(...)):
    return recommend(query)

