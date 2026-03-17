FROM python:3.14-alpine
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app
COPY pyproject.toml uv.lock /app/
RUN uv sync --locked
COPY app /app/app

ENTRYPOINT ["uv", "run", "fastapi", "run", "app/main.py", "--host", "0.0.0.0", "--port", "80"]
