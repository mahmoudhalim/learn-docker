FROM python:3.10.20 AS builder
WORKDIR /build
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3.10.20-slim
WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY hello.py .

ENV PATH=/root/.local/bin:$PATH

EXPOSE 5000
CMD ["python", "hello.py"]
