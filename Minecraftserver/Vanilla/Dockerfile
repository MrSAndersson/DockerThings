FROM openjdk:10-jre-slim

LABEL maintainer="stefan.nigma@gmail.com"
LABEL version="2018.07.13"


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

RUN cd /home/minecraft ; wget https://launcher.mojang.com/mc/game/1.13/server/d0caafb8438ebd206f99930cfaecfa6c9a13dca0/server.jar

RUN mkdir /home/minecraft/server 
WORKDIR /home/minecraft/server

RUN echo "eula=true" > /home/minecraft/server/eula.txt

EXPOSE 25565

VOLUME ["/home/minecraft/server"]

ENTRYPOINT [ "/start.sh" ]