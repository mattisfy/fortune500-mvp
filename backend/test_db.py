import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()  # make sure it reads your .env

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set in .env")

try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as conn:
        result = conn.execute("SELECT 1")
        print("Database connection successful:", result.scalar())
except Exception as e:
    print("Database connection failed:", e)
