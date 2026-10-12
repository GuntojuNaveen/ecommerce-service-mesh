FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY frontend.py .

EXPOSE 5000

CMD ["python", "frontend.py"]
