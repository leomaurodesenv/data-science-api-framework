#!/bin/sh

#-- Variables
APP_IMAGE="data-science-api:0.2.2"
APP_NAME="data-science-api-container"

#-- Introduction message
echo "-----------------------------------------"
echo "Running Data Science API Framework..."
echo "Docker image: $APP_IMAGE"
echo "Docker container: $APP_NAME"
echo "-----------------------------------------"

#-- Docker
# build image
docker build -t $APP_IMAGE .
# running container
docker run -d --name $APP_NAME -p 5050:5050 $APP_IMAGE

#-- Conclusion
echo "-----------------------------------------"
echo "Your API is running..."
echo "API: http://localhost:5050/api/"
echo "-----------------------------------------"
