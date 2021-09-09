# What the Flask

## Getting started
Build the docker image with the following command
```sh
docker-compose build
```

## Running it
Then to run it run
```sh
docker-compose up
```

## Migrations
Running the migrations
```sh
docker-compose exec web bash -c "python server/models.py"
```

Add some test data
```sh
docker-compose exec web bash -c "python server/insert.py"
```
