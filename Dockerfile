FROM python:3.12-slim
WORKDIR /app
COPY agrichainp.py .
CMD ["python", "agrichainp.py"]