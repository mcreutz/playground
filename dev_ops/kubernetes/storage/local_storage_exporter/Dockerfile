# Stage 1: Build the application
FROM python:3.13-slim AS build-stage

WORKDIR /app

COPY . .
RUN python -m venv ./venv
# activate venv
ENV PATH="/app/venv/bin:$PATH"  
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Run the application
FROM python:3.13-slim

WORKDIR /app

COPY --from=build-stage /app .
# activate venv
ENV PATH="/app/venv/bin:$PATH"

CMD ["python", src/local_storage_exporter.py]
