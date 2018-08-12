build:
	docker pull openjdk:8-jre-slim
	docker build . --tag zappka/ftb
	docker tag zappka/ftb zappka/ftb:3.0.2

push:
	docker push zappka/ftb
	docker push zappka/ftb:3.0.2

all: build push
