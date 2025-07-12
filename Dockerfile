FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY app/ app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app/main.py"]
