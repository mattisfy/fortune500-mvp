import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from backend/.env
dotenv_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path)

DATABASE_URL = os.getenv("DATABASE_URL")  # <- the name must be a string!
if not DATABASE_URL:
    raise RuntimeError("Please set DATABASE_URL env var")
from sqlalchemy import create_engine, MetaData

if not DATABASE_URL:
    raise RuntimeError("Please set DATABASE_URL env var")
engine = create_engine(DATABASE_URL)
metadata = MetaData()
