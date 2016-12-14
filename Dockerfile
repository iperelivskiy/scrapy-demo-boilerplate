FROM python:2.7
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
ADD . /code
WORKDIR /code
RUN easy_install -U pip && pip install -r requirements.txt
