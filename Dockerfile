FROM python:3.10.20-alpine3.22

COPY hello.py .

CMD ["python", "hello.py"]
