build:
	docker pull cm2network/steamcmd
	docker build . --tag zappka/ark
	docker tag zappka/ark:latest zappka/ark:$(shell date +%d-%m-%y)

push:
	docker push zappka/ark:latest
	docker push zappka/ark:$(shell date +%d-%m-%y)

all: build push
