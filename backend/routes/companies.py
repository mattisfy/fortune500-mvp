
from fastapi import APIRouter, HTTPException
from ..db import engine
from ..models import companies
from sqlalchemy import select, text

router = APIRouter()

@router.get("/")
def list_companies(q: str = None, limit: int = 50, offset: int = 0):
    conn = engine.connect()
    if q:
        stmt = text("SELECT * FROM companies WHERE name ILIKE :q ORDER BY rank NULLS LAST LIMIT :lim OFFSET :off")
        result = conn.execute(stmt, {"q": f"%{q}%", "lim": limit, "off": offset})
    else:
        stmt = select([companies]).limit(limit).offset(offset)
        result = conn.execute(stmt)
    rows = [dict(r) for r in result]
    conn.close()
    return {"companies": rows}

@router.get("/{company_id}")
def get_company(company_id: int):
    conn = engine.connect()
    stmt = select([companies]).where(companies.c.id == company_id)
    result = conn.execute(stmt).first()
    conn.close()
    if not result:
        raise HTTPException(status_code=404, detail="Company not found")
    return dict(result)
