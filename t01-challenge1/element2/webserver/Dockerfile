FROM python:3.9-slim

WORKDIR /app
COPY . /app

# Simple Flask app example
RUN pip install flask

ENV FLASK_APP=web.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]