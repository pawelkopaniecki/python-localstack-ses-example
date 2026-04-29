FROM python:3.14.4-slim-trixie AS builder

COPY --from=ghcr.io/astral-sh/uv@sha256:72ab0aeb448090480ccabb99fb5f52b0dc3c71923bffb5e2e26517a1c27b7fec /uv /uvx /bin/

ENV UV_PYTHON_DOWNLOADS=0

WORKDIR /app

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-editable

COPY . /app

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-editable

FROM python:3.14.4-slim-trixie

COPY --from=builder /app /app

WORKDIR /app

RUN useradd -r -s /bin/false appuser && chown -R appuser:appuser /app

USER appuser

CMD ["/app/.venv/bin/fastapi", "run", "src/main.py", "--port", "8000", "--host", "0.0.0.0", "--workers", "4"]
