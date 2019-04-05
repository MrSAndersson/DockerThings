build:
	docker pull openjdk:10-jre-slim
	docker build . --tag zappka/minecraft
	docker tag zappka/minecraft zappka/minecraft:1.13.2

push:
	docker push zappka/minecraft
	docker push zappka/minecraft:1.13.2

all: build push
