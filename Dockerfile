FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /e-leave
WORKDIR /e-leave
COPY requirements.txt /e-leave/
RUN pip install -r requirements.txt
COPY . /e-leave/
