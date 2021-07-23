FROM python:3.7

WORKDIR /code
COPY requirements.txt /code
RUN pip install -r /code/api_server/requirements.txt
COPY . /code
WORKDIR /code/api_server/
RUN gunicorn api.wsgi:application 0.0.0.0:8000