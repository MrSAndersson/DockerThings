build:
	docker pull openjdk:10-jre-slim
	docker build . --tag zappka/minecraft
	docker tag zappka/minecraft zappka/minecraft:1.12.2

push:
	docker push zappka/minecraft

all: build push
