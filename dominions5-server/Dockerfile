FROM cm2network/steamcmd

USER root
RUN apt-get update ; apt-get install -y libsdl2-2.0-0 libglu1 libgl1-mesa-glx wget lsb-release procps unzip ; rm -rf /var/lib/apt/lists/*
USER steam

RUN mkdir /home/steam/dom5 /home/steam/.dominions5
VOLUME ["/home/steam/dom5"]
VOLUME [ "/home/steam/.dominions5" ]

COPY --chown=steam:steam dom5-init.sh /home/steam/dom5-init.sh
COPY --chown=steam:steam AI_No_RecruitV.6.zip /home/steam/AI_No_RecruitV.6.zip

RUN chmod u+x /home/steam/dom5-init.sh

WORKDIR /home/steam
EXPOSE 7777/tcp

ENTRYPOINT [ "/home/steam/dom5/dom5.sh", "-TS", "--era", "1", "--renaming", "--masterpass", "grob", \
    "--diffai", "14", "--normai", "8", "--diffai", "11", "--diffai", "38", \
    "--thrones", "0", "8", "0", "--requiredap", "8", \
    "--port", "7777", "--hours", "62", "--nosteam", "--mapfile", "FloatingArchipelago.map", "Grobminions5" ]
