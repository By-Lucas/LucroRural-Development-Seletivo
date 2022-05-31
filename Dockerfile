FROM python:3.9.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBFFERED 1

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .