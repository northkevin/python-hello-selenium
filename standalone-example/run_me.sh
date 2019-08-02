#!/bin/sh

docker-compose -f ./docker-compose.yaml up --build -d

export SELENIUM_SERVICE_NAME="selenium-standalone-chrome"
export SELENIUM_IP=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $SELENIUM_SERVICE_NAME)
export SELENIUM_PORT="4444"
export SELENIUM_BROWSER="CHROME"

docker-compose -f docker-compose.yaml exec test-scripts python selenium-test/check_browser.py --browser=$SELENIUM_BROWSER --port=$SELENIUM_PORT --ip=$SELENIUM_IP