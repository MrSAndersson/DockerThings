build:
	docker pull grafana/grafana
	docker build . --tag zappka/phmeter

push:
	docker push zappka/phmeter

all: build push
