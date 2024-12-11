From python:3.13-slim

WORKDIR /app

RUN pip install aiohttp aiobotocore python-dotenv

COPY main.py main.py

CMD ["python", "-u", "main.py"]
