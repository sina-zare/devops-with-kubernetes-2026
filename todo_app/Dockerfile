
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --index-url https://repo.abramad.com/repository/pypi-proxy/simple --trusted-host repo.abramad.com

COPY app.py .

ENV PORT=8080
EXPOSE 8080

CMD ["python", "app.py"]