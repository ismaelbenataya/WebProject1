FROM python:3.11

ENV PYTHONUNBUFFERED 1

RUN mkdir /web1
WORKDIR /web1
COPY requirements.txt /web1/
RUN pip install -r requirements.txt
COPY . /web1/