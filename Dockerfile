FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml README.md ./
COPY hr_compliance_mcp ./hr_compliance_mcp

RUN pip install --no-cache-dir ".[api]"

ENV PORT=8000
EXPOSE 8000

CMD ["sh", "-c", "uvicorn hr_compliance_mcp.api.app:app --host 0.0.0.0 --port ${PORT}"]
