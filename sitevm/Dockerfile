FROM python:3

RUN python -m pip install django 

RUN pip install psycopg2-binary

RUN mkdir -p /opt/app

COPY . /opt/app

WORKDIR /opt/app

ENTRYPOINT python manager.py runserver