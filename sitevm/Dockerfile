FROM python:3

RUN python -m pip install django 

RUN pip install psycopg2-binary

RUN mkdir -p /opt/app

COPY . /opt/app

EXPOSE 8000

WORKDIR /opt/app

ENTRYPOINT python manage.py runserver