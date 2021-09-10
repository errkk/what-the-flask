build:
	docker-compose build

dev:
	docker-compose up

bash:
	docker-compose exec web bash

init_db:
	docker-compose exec web bash -c "psql -h postgres -U postgres -c 'create database flaskexample;'"

migrate:
	docker-compose exec web bash -c "flask db migrate"

upgrade:
	docker-compose exec web bash -c "flask db upgrade"

flask_shell:
	docker-compose exec web bash -c "flask shell"
