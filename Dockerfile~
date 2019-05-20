FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /employee-leave
WORKDIR /employee-leave
COPY requirements.txt /employee-leave/
RUN pip install -r requirements.txt
COPY . /employee-leave/
