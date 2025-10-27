
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes.companies import router as companies_router
from dotenv import load_dotenv
import os
load_dotenv()

app = FastAPI(title="Fortune500 API (MVP)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(companies_router, prefix="/api/companies")

@app.get("/health")
def health():
    return {"status":"ok"}
