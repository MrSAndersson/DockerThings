FROM fedora

RUN dnf install -y fedora-packager fedora-review make; dnf clean all
RUN useradd -m -G mock stefan

USER stefan
WORKDIR /home/stefan

ADD --chown=stefan:stefan . . 

ENTRYPOINT [ "bash" ]