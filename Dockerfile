FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
ADD . /code
WORKDIR /code
RUN easy_install -U pip && pip install -r requirements.txt
