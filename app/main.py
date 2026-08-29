from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app.api.routes import router as api_router

app = FastAPI(title="Resume Analyzer", version="1.0.0")
app.include_router(api_router, prefix="/api")


@app.get("/", response_class=HTMLResponse)
def health_check():
    html_path = Path(__file__).parent / "templates" / "index.html"
    return HTMLResponse(content=html_path.read_text(encoding="utf-8"))
