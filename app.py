from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from recommender import recommend

app = FastAPI()

# Templates folder
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "results": []})

@app.post("/search", response_class=HTMLResponse)
async def search_keyword(request: Request, keyword: str = Form(...)):
    results = recommend(keyword, top_n=5)
    return templates.TemplateResponse("index.html", {"request": request, "results": results, "keyword": keyword})

