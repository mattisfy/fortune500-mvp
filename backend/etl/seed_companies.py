
# Simple CSV importer for companies (use with DATABASE_URL set)
import csv, os

from dotenv import load_dotenv
from pathlib import Path

# Load .env from backend folder
dotenv_path = Path(__file__).parent.parent / ".env"  # ../.env relative to etl/
load_dotenv(dotenv_path)

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("Please set DATABASE_URL in backend/.env")

from sqlalchemy import create_engine, text
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

def import_csv(path):
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        with engine.begin() as conn:
            for row in reader:
                conn.execute(text("""
                INSERT INTO companies (name, ticker, rank, industry, headquarters, website, description, logo_url)
                VALUES (:name, :ticker, :rank, :industry, :hq, :website, :description, :logo)
                ON CONFLICT (name) DO NOTHING
                """), {
                    "name": row.get("name"),
                    "ticker": row.get("ticker"),
                    "rank": int(row.get("rank")) if row.get("rank") else None,
                    "industry": row.get("industry"),
                    "hq": row.get("headquarters"),
                    "website": row.get("website"),
                    "description": row.get("description"),
                    "logo": row.get("logo_url")
                })

if __name__ == '__main__':
    import_csv("../../infra/sample_companies.csv")
