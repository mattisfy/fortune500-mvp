
# Fortune500-DB MVP

This repository contains a full scaffold for a low-cost, portable MVP for a Fortune 500 company database site.
It uses:
- Frontend: Next.js (React) - deploy to Vercel or Netlify
- Backend: FastAPI (Python) - deploy to Render or Fly.io
- Database: Supabase (Postgres) - free tier recommended
- ETL: Python scripts (Alpha Vantage + GNews)
- CI: GitHub Actions for scheduled ETL

This zip includes code and a step-by-step instruction sheet (below) for creating accounts, deploying, and monetization hooks.

## Quick structure
- backend/
  - main.py
  - db.py
  - models.py
  - routes/companies.py
  - etl/seed_companies.py
  - requirements.txt
  - Dockerfile
- frontend/
  - package.json
  - next.config.js
  - pages/index.js
  - pages/company/[id].js
  - components/Layout.js
  - public/ (logo placeholder)
- infra/
  - schema.sql
  - sample_companies.csv
  - .github/workflows/etl.yml

## Download & Use
Unzip and follow the Instructions below (also included in this README).

