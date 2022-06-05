## LocalInflux

Simple InfluxDB container with basic write API deployed in a trust environment (e.g. local network) that does not require authentication to add data points.

### Requirements

- [docker](https://docs.docker.com/get-docker/)
- [docker-compose](https://docs.docker.com/compose/install/)

### Usage

```bash
git clone https://github.com/ungineer/localinflux
cd localinflux
mkdir data
# you might need to run this with sudo, depending on your install
docker-compose up -d
# docker compose up -d <-- for newer docker installations
```

Now you should be able to access the basic UI at http://localhost:8400/docs

The influxDB ui is accessible at http://localhost:8086. Username: "admin" password: "099876admin".
