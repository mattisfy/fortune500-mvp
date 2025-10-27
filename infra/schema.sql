
-- Minimal schema for MVP
CREATE TABLE IF NOT EXISTS companies (
  id SERIAL PRIMARY KEY,
  name TEXT UNIQUE NOT NULL,
  ticker TEXT,
  rank INTEGER,
  industry TEXT,
  headquarters TEXT,
  website TEXT,
  description TEXT,
  logo_url TEXT,
  last_updated TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX IF NOT EXISTS companies_name_idx ON companies USING gin (to_tsvector('english', name));
