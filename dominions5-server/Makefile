build:
	docker-compose build --pull

up: build down
	docker-compose up -d

down:
	docker-compose down

shell: build down
	docker-compose run --entrypoint bash dom5
