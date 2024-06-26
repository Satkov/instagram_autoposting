FROM python:3.8.5

WORKDIR /code
COPY requirements.txt /code
RUN pip install -r /code/requirements.txt
COPY . /code
RUN cd /code
CMD gunicorn api_server.api.wsgi:application --bind 0.0.0.0:8000