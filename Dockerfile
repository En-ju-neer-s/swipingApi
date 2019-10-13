# Simple Dockerfile can be expanded
FROM python:3.7

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python3"]

CMD ["start.py"]