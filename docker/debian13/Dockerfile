# Use Debian 13 (Trixie)
FROM debian:trixie

# Install prerequisites (SSH and Python3 for Ansible)
RUN apt-get update && apt-get install -y \
    openssh-server \
    sudo \
    python3 \
    python3-venv \
    python-is-python3

RUN useradd -m -s /bin/bash -G sudo odradekk && \
    echo 'odradekk:fukk' | chpasswd

RUN sed -i 's/^#\?PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config

# Expose the SSH port
EXPOSE 22

# Start the SSH server in the foreground
CMD ["/usr/sbin/sshd", "-D"]