FROM python:3

WORKDIR /app

RUN apt-get clean && apt-get update && apt-get install -y locales
RUN sed -i -e 's/# pt_BR.UTF-8 UTF-8/pt_BR.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen

COPY ./requirements.txt /app
RUN pip install -r /app/requirements.txt

COPY . /app
