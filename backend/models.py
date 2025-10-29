
from sqlalchemy import Table, Column, Integer, String, Text, DateTime, Numeric
from sqlalchemy.sql import func
from db import metadata

companies = Table(
    "companies",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("ticker", String),
    Column("rank", Integer),
    Column("industry", String),
    Column("headquarters", String),
    Column("website", String),
    Column("description", Text),
    Column("logo_url", String),
    Column("last_updated", DateTime, server_default=func.now())
)
