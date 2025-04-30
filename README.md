# Simple App Example

## Create virtual environment
```shell
conda env create -f environment.yml
```

## Run app in dev mode
```shell
fastapi dev main.py
```
## Test in dev mode
```shell
curl -X 'POST' \
  'http://127.0.0.1:8000/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "test item",
  "description": "test",
  "value": 100
}'
```

## Run tests
```shell
pytest tests
```

## Build docker image
```shell
docker build -t simple-app .
```

## Start docker container
```shell
docker run -d --name simple-app-container -p 80:80 simple-app
```

## Test containerized application
```shell
curl -X 'POST' \
  'http://localhost:80/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "test item",
  "description": "test",
  "value": 100
}'
```