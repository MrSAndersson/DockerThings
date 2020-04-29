build:
	docker pull ubuntu
	docker build . --tag zappka/minecraft-bedrock:latest

push:
	docker push zappka/minecraft-bedrock:latest

all: build push
