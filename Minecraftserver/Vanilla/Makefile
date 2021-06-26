build:
	docker pull openjdk:jre-slim
	docker build . --tag zappka/minecraft:latest
	docker tag zappka/minecraft zappka/minecraft:1.17

push:
	docker push zappka/minecraft:latest
	docker push zappka/minecraft:1.17

all: build push
