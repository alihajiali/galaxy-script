From python:3.13-slim

WORKDIR /app

RUN pip install aiohttp aiobotocore

COPY main.py main.py

CMD ["python", "-u", "main.py"]
