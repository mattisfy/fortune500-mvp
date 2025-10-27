
Paywall + API key plan (instructions)

1. Add a `users` table in Postgres and integrate Supabase Auth or JWT-based auth.
2. Create `api_keys` table with owner, plan, quota, secret.
3. Add middleware in FastAPI to check for `X-API-KEY` header and enforce quotas (store counters in DB or Redis).
4. Integrate Stripe to accept payments and provision API keys automatically on success.
