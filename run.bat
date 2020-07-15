@ECHO OFF

::-- Variables
SET APP_IMAGE=data-science-api:0.2.1
SET APP_NAME=data-science-api-container

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
docker run -d --name %APP_NAME% -p 5050:5050 %APP_IMAGE%

::-- Conclusion
ECHO -----------------------------------------
ECHO Your API is running...
ECHO API: http://localhost:5050/api/
ECHO -----------------------------------------
