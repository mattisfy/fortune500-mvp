
# Step-by-step Instructions: Accounts, Setup, Deploy, Monetize

This document walks you through creating required accounts, setting up the project, deploying, and monetization options. Follow in order.

--- 
PREREQS (local)
- Git installed
- Node.js (v18+) and npm
- Python 3.10+ and pip
- GitHub account

## Accounts to create (order)
1. **GitHub** (for repo & CI) - https://github.com
2. **Cloudflare** (DNS + optional CDN) - https://dash.cloudflare.com
3. **Supabase** (Postgres DB) - https://supabase.com
4. **Render** (Backend hosting) or **Fly.io** - https://render.com / https://fly.io
5. **Vercel** or **Netlify** (Frontend host) - https://vercel.com or https://netlify.com
6. **Alpha Vantage** (stock API) - https://www.alphavantage.co
7. **GNews** (news API) - https://gnews.io
8. **UptimeRobot** (monitoring) - https://uptimerobot.com
9. **Stripe** (for later paywall) - https://stripe.com

Store API keys and credentials in a secure password manager.

---

## Local setup (development)

1. Clone this repo to your machine:
   ```bash
   git clone <your-repo-url>
   cd fortune500-mvp
   ```

2. Backend setup
   - Create Python virtualenv:
     ```bash
     python -m venv venv
     source venv/bin/activate
     pip install -r backend/requirements.txt
     ```
   - Configure environment variables (create `.env` in backend/):
     ```
     DATABASE_URL=<your_supabase_db_url>
     ALPHA_VANTAGE_KEY=<your_alpha_vantage_key>
     GNEWS_KEY=<your_gnews_key>
     ```
   - Run locally:
     ```bash
     uvicorn backend.main:app --reload --port 8000
     ```
   - Test endpoint: `http://localhost:8000/health` and `http://localhost:8000/api/companies`

3. Frontend setup
   - Install:
     ```bash
     cd frontend
     npm install
     npm run dev
     ```
   - Visit `http://localhost:3000`

4. Seed sample data into Supabase
   - Use Supabase SQL editor to run `infra/schema.sql`
   - Use Supabase UI to import `infra/sample_companies.csv` into `companies` table
   - Or run backend ETL script to seed (see below).

---

## Deployment (MVP)

### Supabase
- Create project → note `DATABASE_URL` (or connection string)
- Run `infra/schema.sql` in SQL editor
- Import `sample_companies.csv` or run ETL.

### Render (Backend)
- Create new Web Service → connect to GitHub repo
- Build command: `pip install -r backend/requirements.txt`
- Start command: `uvicorn backend.main:app --host 0.0.0.0 --port 10000`
- Set env vars in Render dashboard: `DATABASE_URL`, `ALPHA_VANTAGE_KEY`, `GNEWS_KEY`
- Deploy

### Vercel / Netlify (Frontend)
- Connect repo and set environment variable `API_BASE_URL` to your Render service URL (e.g., `https://your-api.onrender.com`)
- Deploy

### DNS (Cloudflare)
- Point `www` CNAME to Vercel/Netlify
- Create `api` CNAME to Render hostname
- Configure SSL (Cloudflare will proxy; set SSL mode to Full)

### GitHub Actions ETL
- The included workflow runs daily to fetch stock & news and push into the DB.
- Ensure repository secrets set: `DATABASE_URL`, `ALPHA_VANTAGE_KEY`, `GNEWS_KEY`

---

## Monetization hooks (how to implement later)
1. **Ads**: Add Google AdSense snippet to `frontend/components/Layout.js` or appropriate pages.
2. **Paid API**: Add API key / rate limit middleware in backend; create Stripe subscription endpoints. (See `backend/README_PAYWALL.md`).
3. **CSV/Export**: Add a premium route to download full CSV export; protect it with JWT.
4. **Newsletter**: Use Mailchimp/Sendgrid to collect signups and send sponsored newsletters.

---

## IMDB-like Navigation & Data-Structure Notes
- Main nav: Home | Browse (by rank/industry) | Companies | People | News | API | About
- Company page layout: Header (name, rank, ticker), Tabs: Overview | Stock | Executives | News | Connections
- Person page: Bio, Employment timeline, Education, Connections
- Use JSON-LD for SEO and AI-friendliness

---

For more detailed operational commands, see the `backend/` and `frontend/` READMEs.

