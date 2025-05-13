# Simple App Example

Example of setting up a cloud native application using FastAPI, Docker, Pytest, GitHub Actions, and Kubernetes.

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

## GitHub Actions
Several tests will run when there is a push or pull request to the git main branch.
These are defined in [./github/workflows/](.github/workflows/) and include:

- run pytests (see [./tests/](tests/))
- build and test docker container

## Next Steps
1. Set up local Kubernetes cluster using Minikube. Deploy containerized app.
2. Update set up to include more than one microservice.
