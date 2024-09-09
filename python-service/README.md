# Python Service

## install
pip install -r requirements.txt

## Run
fastapi dev main.py

## prod run
fastapi main.py

## Docker build
docker build -t python-service .

## Docker run
docker run -p 8000:8000 --name python-service --rm python-service

# test
curl localhost:8000/index

# doc
localhost:8000/docs

