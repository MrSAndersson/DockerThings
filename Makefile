all: build

build:
	docker pull grafana/grafana
	cd ./PH-Meter && docker build .
