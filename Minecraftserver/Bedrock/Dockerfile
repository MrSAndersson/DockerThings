FROM ubuntu

LABEL maintainer="stefan.svard@gmail.com"
LABEL version="1.14.60.05"

# Set timezone in container
ENV TZ=Europe/Stockholm
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update ; apt-get install -y libcurl4 ; rm -rf /var/lib/apt/lists/*

RUN useradd minecraft -m
USER minecraft

WORKDIR /home/minecraft
RUN mkdir worlds

COPY bedrock-server/ .
COPY server.properties .


EXPOSE 19132

VOLUME ["/home/minecraft/worlds"]
ENV LD_LIBRARY_PATH /home/minecraft/
ENTRYPOINT [ "./bedrock_server" ]
