from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from app.routes import contact

app = FastAPI(
    title="Hagop Hadjiakian Portfolio API",
    description="Backend API for the portfolio website",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://hagophadjiakian2028.up.railway.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(contact.router, prefix="/api", tags=["contact"])

# Serve static files from assets folder
assets_path = Path(__file__).parent.parent / "assets"
if assets_path.exists():
    app.mount("/assets", StaticFiles(directory=str(assets_path)), name="assets")


@app.get("/")
async def root():
    return {"message": "Welcome to Hagop Hadjiakian's Portfolio API"}


@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}
