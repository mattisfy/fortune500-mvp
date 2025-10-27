# create_tables.py
from db import engine, metadata  # ensure this imports backend/db.py and your metadata from models.py
from models import companies      # import your table definitions so they are registered with metadata

# Create all tables defined in metadata
metadata.create_all(engine)
print("All tables created successfully!")
