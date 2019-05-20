FROM python:3
MAINTAINER Mkhululi Tyukala <mkhululi.tyukala@gmail.com>
ENV PYTHONUNBUFFERED 1
RUN mkdir /e-leave
WORKDIR /e-leave
COPY requirements.txt /e-leave/
RUN pip install -r requirements.txt
COPY . /e-leave/
