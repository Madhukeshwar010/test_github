FROM python:3.12-slim

WORKDIR /app

COPY sensor_read.py ./

CMD ["python", "sensor_read.py"]
