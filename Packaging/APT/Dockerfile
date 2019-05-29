FROM ubuntu

RUN apt-get update ; apt-get install dh-make bzr-builddeb ; apt-get -y autoremove ; rm -rf /var/lib/apt/lists/*

VOLUME /build

ENTRYPOINT [ "/bin/bash" ]
