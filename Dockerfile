#-- Define the startup image
# container image = python:3
FROM python:3

#-- Define the labels
LABEL maintainer="Leonardo Mauro <leomaurodesenv>"
LABEL version="0.2.1"

#-- Working directory
# it will be virtualized in docker run
COPY . /app
WORKDIR /app

#-- Python requirements
RUN pip install --no-cache-dir -r ./requirements.txt

#-- API port
EXPOSE 5050

#-- Running api
CMD [ "python", "./app/daemon.py" ]