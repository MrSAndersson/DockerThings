build:
	docker pull ubuntu
	docker build . --tag zappka/minecraft-bedrock:latest
	docker tag zappka/minecraft-bedrock:latest zappka/minecraft-bedrock:1.14.60.05

push:
	docker push zappka/minecraft-bedrock:latest
	docker push zappka/minecraft-bedrock:1.14.60.05

all: build push
