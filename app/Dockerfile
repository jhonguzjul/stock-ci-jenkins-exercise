FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/src

WORKDIR /app
COPY src/ ./src/

RUN useradd --create-home --uid 10001 app
USER app

EXPOSE 8000
CMD ["python", "-m", "inventario"]
