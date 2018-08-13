FROM openjdk:8-jre-slim

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

RUN mkdir /home/minecraft/zip ; \
    cd /home/minecraft/zip ; \
    wget https://www.feed-the-beast.com/projects/ftb-infinity-evolved/files/2484486/download ; \
    unzip download ; \
    rm download ; \
    wget https://minecraft.curseforge.com/projects/revamp/files/latest ; \
    mv latest mods/Revamp.jar
# COPY --chown=minecraft:minecraft ServerStart.sh /home/minecraft/zip/
RUN chmod +x /home/minecraft/zip/ServerStart.sh

RUN mkdir /home/minecraft/server 
WORKDIR /home/minecraft/server

RUN echo "eula=true" > /home/minecraft/zip/eula.txt

EXPOSE 25565

VOLUME ["/home/minecraft/server"]

ENTRYPOINT [ "/start.sh" ]