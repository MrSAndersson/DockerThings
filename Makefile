build:
	docker pull grafana/grafana
	cd ./PH-Meter && docker build . --tag zappka/phmeter

push:
	docker push zappka/phmeter

all: build push
