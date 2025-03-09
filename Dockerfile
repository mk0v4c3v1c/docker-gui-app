FROM python:3.12-slim

LABEL authors="l0sm1sh9"

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "run.py"]
