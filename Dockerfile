FROM tiangolo/uwsgi-nginx-flask:python3.8

EXPOSE 80

COPY ./app /app
