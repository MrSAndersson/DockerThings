all: build run

build:
	docker build . -t rpm-builder

run:
	docker run -it --rm -v build-output:/home/stefan/build-output rpm-builder