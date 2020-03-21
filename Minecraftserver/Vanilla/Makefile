build:
	docker pull openjdk:jre-slim
	docker build . --tag zappka/minecraft:latest
	docker tag zappka/minecraft zappka/minecraft:1.15.2

push:
	docker push zappka/minecraft:latest
	docker push zappka/minecraft:1.15.2

all: build push
