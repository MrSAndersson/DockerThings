FROM cm2network/steamcmd

LABEL maintainer="stefan.nigma@gmail.com"
LABEL version="2019.01.02"

RUN mkdir /home/steam/ark
VOLUME ["/home/steam/ark"]

COPY --chown=steam:steam ark-init.sh /home/steam/ark-init.sh

RUN chmod u+x /home/steam/ark-init.sh

EXPOSE 7777/udp
EXPOSE 7778/udp
EXPOSE 27015/udp
EXPOSE 27020/tcp

ENTRYPOINT [ "/home/steam/ark-init.sh" ]