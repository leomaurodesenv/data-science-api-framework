#-- Define image
FROM python:3.8-slim

#-- Define the labels
LABEL maintainer="Leonardo Mauro <leomaurodesenv>"
LABEL project="data-science-api-framework"

#-- App predefinitions
ENV APP_HOME /app
WORKDIR $APP_HOME

ENV LISTEN_PORT 8080
EXPOSE 8080

#-- Python requirements
RUN python -m pip install --upgrade pip
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

#-- Project
COPY . ./
CMD gunicorn -w 2 -b :8080 -k uvicorn.workers.UvicornWorker app.main:API
