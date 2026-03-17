FROM python:3.14-alpine
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app
COPY . /app/
RUN uv sync --locked

ENTRYPOINT ["uv", "run", "fastapi", "run", "--host", "0.0.0.0", "--port", "80"]