#-- Define the startup image
# image from https://github.com/tiangolo/uwsgi-nginx-flask-docker
FROM tiangolo/uwsgi-nginx-flask:python3.8

#-- Define the labels
LABEL maintainer="Leonardo Mauro <leomaurodesenv>"
LABEL version="0.3.3"

ENV LISTEN_PORT 5050
EXPOSE 5050

#-- Working directory
# it will be virtualized in docker run
COPY ./app /app
COPY ./requirements.txt /app

#-- Python requirements
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt
