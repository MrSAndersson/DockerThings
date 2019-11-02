FROM fedora

RUN dnf install -y gpg pinentry fedora-packager fedora-review make; dnf clean all
RUN useradd -m -G mock stefan

USER stefan
WORKDIR /home/stefan

RUN mkdir /home/stefan/build-output

ADD --chown=stefan:stefan . . 

RUN chmod +x gpg-import.sh

ENTRYPOINT [ "bash" ]