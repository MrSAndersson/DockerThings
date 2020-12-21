build:
	docker pull cm2network/steamcmd
	docker build . --tag dom5

up: build down
	docker run --restart always -d -v dom5-save:/homoe/steam/dom5 -v dom5:/home/steam/dom5 \
    	-p 7777:7777/tcp \
    	--name=dom5 dom5

down:
	docker kill dom5 || true
	docker rm dom5 || true

shell: build down
	docker run -it -v dom5-save:/homoe/steam/dom5 -v dom5:/home/steam/dom5 \
    	-p 7777:7777/tcp --entrypoint bash \
    	--name=dom5 dom5
