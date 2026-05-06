# REST API Deploy Guide

End-to-end checklist for getting the FastAPI surface live on Render. ~15 minutes.

## Prereqs

- GitHub account that owns `Mahender22/hr-compliance-mcp` (already done)
- Render account (free signup at render.com)
- The repo pushed to GitHub (`main` branch contains `Dockerfile` + `render.yaml`)

## 1. Render account

1. Sign up at render.com using your GitHub login
2. Authorize Render to read your repos (limit to `Mahender22/hr-compliance-mcp` only — don't grant all-repo access)

## 2. First deploy via Blueprint

1. Render dashboard → **New → Blueprint**
2. Pick `Mahender22/hr-compliance-mcp`
3. Render reads `render.yaml`, shows: 1 web service `hr-compliance-api`, free plan, Docker runtime
4. Click **Apply**. First build ≈ 3-5 min (Docker cold build)
5. Service URL appears: `https://hr-compliance-api-XXXX.onrender.com`

## 3. Generate first API keys

For onboarding the first 5-10 paying customers manually (no Stripe yet):

```python
# locally, in a Python REPL
import secrets
print(f"hrk_{secrets.token_urlsafe(24)}")
```

Generate one Starter and one Pro key. Save these somewhere safe (1Password, etc.).

## 4. Set environment variable

1. Render dashboard → `hr-compliance-api` → **Environment** tab
2. Add the `HR_API_KEYS` secret as JSON:
   ```json
   {
     "hrk_REPLACE_WITH_STARTER_KEY": "starter",
     "hrk_REPLACE_WITH_PRO_KEY": "pro"
   }
   ```
3. Save. Render auto-redeploys (≈ 1 min)

## 5. Smoke test

```bash
# Health check (no auth)
curl https://hr-compliance-api-XXXX.onrender.com/healthz

# Wage endpoint (Starter+)
curl https://hr-compliance-api-XXXX.onrender.com/v1/wage/CA \
  -H "X-API-Key: hrk_YOUR_STARTER_KEY"

# Pro endpoint (should 402 with starter key)
curl -i https://hr-compliance-api-XXXX.onrender.com/v1/compliance/discrimination/CA \
  -H "X-API-Key: hrk_YOUR_STARTER_KEY"

# Pro endpoint (should 200 with pro key)
curl https://hr-compliance-api-XXXX.onrender.com/v1/compliance/discrimination/CA \
  -H "X-API-Key: hrk_YOUR_PRO_KEY"
```

Cold-start note: free tier spins down after 15 min idle. First request after a sleep takes ≈ 30s. Subsequent requests are fast. For real customers, upgrade to **Starter ($7/mo)** to keep the service warm.

## 6. OpenAPI explorer

`https://hr-compliance-api-XXXX.onrender.com/docs` — FastAPI's auto-generated Swagger UI. Send this URL to prospective customers; they can try every endpoint with their key.

## 7. Custom domain (optional, when ready)

1. Render → service → **Settings → Custom Domain → Add**
2. Use `api.hrcompliance.dev` (assuming you've registered the domain per `hr-compliance-site/DEPLOY.md`)
3. Cloudflare DNS: add CNAME `api → <service>.onrender.com`, **DNS only** (gray cloud)
4. Render provisions SSL automatically (Let's Encrypt)

## 8. Onboard first customer

1. Generate a unique key with `secrets.token_urlsafe(24)`
2. Add it to `HR_API_KEYS` env var in Render (append to JSON, redeploys)
3. Send the customer:
   - Their key
   - The `https://api.hrcompliance.dev/docs` URL
   - The `/v1/states` endpoint (free, no auth) so they can verify connectivity

## 9. When to add Stripe

When you have **3+ inbound paying customers asking for self-serve signup**. Until then, manual onboarding is faster and gives you direct usage feedback. Stripe Checkout + a tiny `/stripe/webhook` handler that mutates the keys table is ~150 lines of code; not worth writing speculatively.

## Cost summary

| Item | When | Cost |
|---|---|---|
| Render free | always (cold-start trade-off) | $0 |
| Render starter | once first customer wants warm latency | $7/mo |
| Custom domain (already registered for site) | reuse | $0 |
| **Total to launch** | — | **$0** |
