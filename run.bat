@ECHO OFF

::-- Variables
SET APP_IMAGE=ds-api
SET APP_NAME=ds-api-container

::-- Introduction message
TITLE Data Science API Framework
ECHO -----------------------------------------
ECHO Running Data Science API Framework...
ECHO Docker image: %APP_IMAGE%
ECHO Docker container: %APP_NAME%
ECHO -----------------------------------------

::-- Docker
:: build image
docker build -t %APP_IMAGE% .
:: running container
docker run --rm -it --name %APP_NAME% -p 5050:5050 %APP_IMAGE%
