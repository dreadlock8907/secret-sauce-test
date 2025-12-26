@echo off

echo Launching tests in Docker...
docker-compose up --build
echo To stop the report server: docker-compose down
echo .
pause
