FROM debian

RUN apt-get update && apt-get install -y \
    openssh-server python sudo systemd \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/bash stefan && \
    echo "stefan ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
COPY --chown=stefan:stefan authorized_keys /home/stefan/.ssh/

COPY ssh_host_* /etc/ssh/
RUN chmod 600 /etc/ssh/ssh_host_*_key

CMD ["/sbin/init"]
