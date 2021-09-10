# What the Flask

## Getting started
Build the docker image with the following command
```sh
make build
```

## Running it
Then to run it run
```sh
make dev
```
This will start the Docker container, which will be running the development webserver on port 5000
You can visit the site at http://localhost:5000
This also needs to be running in order to exectute commands on the container. See below

## Database
First to setup the database, with the containers running (`make dev`) you need to create the DB:
```sh
make init_db
```
You only need to do this once. Then the database is created, you should be able to see it now in Table Plus.

### Update schema version with migrations
To run the migrations
```sh
make upgrade
```

To create a new migration, when you update the models
```sh
make migrate
```
Here, Alembic will look at the current database, and see what's different in the models. The changes will be written into a version file in `/migrations/versions`, you should edit this to contain a description, and make sure the migration does what you need. Give the file a descriptive name and the run `make upgrade` to apply the changes.

### Test data
Add some test data
```sh
docker-compose exec web bash -c "python server/insert.py"
```
