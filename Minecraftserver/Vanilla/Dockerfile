FROM openjdk:jre-slim

LABEL maintainer="stefan@svard.me"
LABEL version="1.17"


# Switch to root user in order to install things
USER root

# Set timezone in container
ENV TZ=Europe/Stockholm
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update ; apt-get install --no-install-recommends -y wget vim ; rm -rf /var/lib/apt/lists/*

COPY start.sh /
RUN chmod +x start.sh

RUN useradd minecraft -m
USER minecraft

RUN cd /home/minecraft ; wget https://launcher.mojang.com/v1/objects/0a269b5f2c5b93b1712d0f5dc43b6182b9ab254e/server.jar

RUN mkdir /home/minecraft/server 
WORKDIR /home/minecraft/server

RUN echo "eula=true" > /home/minecraft/server/eula.txt

EXPOSE 25565

VOLUME ["/home/minecraft/server"]

ENTRYPOINT [ "/start.sh" ]
