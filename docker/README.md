# Docker

An assembly of Dockerfiles and instructions I find useful for different purposes.

## Debian 13 (Trixie)

In directory `debian13`. Used for testing Ansible Playbooks.
Set up a Docker network with a subnet via

```bash
docker network create -d bridge \
  --subnet=172.20.0.0/16 \
  --gateway=172.20.0.1 \
  my-ansible-net
```

Go to the `debian13` directory and build the image and spin up the container:
```bash
cd debian13
docker build -t debian-ansible-test .
docker run -d \
  --name ansible-target \
  --network my-ansible-net \
  --ip 172.20.0.5 \
  -p 2222:22 \
  debian-ansible-test
```

The IP-address `172.20.0.5` will be the one you need to add to your hosts section in ansibles `inventory.ini`.

## General tips

Reset the root password in a container:
```bash
docker exec -itu 0 {container} passwd
```