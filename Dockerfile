#-- Define the startup image
FROM tiangolo/meinheld-gunicorn-flask:python3.7

#-- Define the labels
LABEL maintainer="Leonardo Mauro <leomaurodesenv>"
LABEL version="0.4.4"

ENV LISTEN_PORT 5050
EXPOSE 5050

#-- Python requirements
RUN python -m pip install --upgrade pip
# requirements.txt
COPY ./requirements.txt /app
RUN pip install --no-cache-dir -r /app/requirements.txt

#-- Working directory
# it will be virtualized in docker run
COPY ./app /app
