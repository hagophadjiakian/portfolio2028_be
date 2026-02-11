from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

# Assets are now served from the frontend
# Static file serving removed to reduce backend memory usage


@app.get("/")
async def root():
    return {"message": "Welcome to Hagop Hadjiakian's Portfolio API"}


@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}
