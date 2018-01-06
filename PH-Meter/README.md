# PH-Meter
Bundles Mosquitto, InfluxDB and Grafana to receive and display PH-Meter data.
Available with docker image 'zappka/phmeter'

## Configuration

Many aspects of the container can be customized by defining environment variables when running it.

### Grafana

Grafana can be configured and customized the same ways that the official  'grafana/grafana' image can.

Examples of possible customizations:

* Setting of 'admin' user password (needed to customize dashboards as the default password is randomized)
```
-e "GF_SECURITY_ADMIN_PASSWORD=<grafana-admin-password>"
```
* Allowing anonymous users
```
-e "GF_AUTH_ANONYMOUS_ENABLED=true"
```
* Server URL
```
-e "GF_SERVER_ROOT_URL=http://<your-server-root>"
```
* Installation of plugins

Here is the official Grafana Docker documentation: https://hub.docker.com/r/grafana/grafana/

Grafana port within container: 3000

### Mosquitto

Mosquitto is currently set up with two users: 'phmeter' and 'user'. Both have strong randomized passwords by default so you need to set a password for each user you want to use by adding corresponding environment variables:

```
-e "MOSQ_PHMETER_PASS=<your-phmeter-password>"
-e "MOSQ_USER_PASS=<your-user-password>"
```
Mosquitto ports within container: 1883 for regular traffic and 8883 for SSL

## Persisting Data

In order to persist data, a VOLUME is exposed in the image.
```
-v phdata:/var/lib/influxdb
```

## Interaction

## SSL

In case you want to use SSL/TLS, your best bet is to create a reverse proxy in front of the container using Apache, NGINX or somthing similar. For SSL certificates, [Letsencrypt](https://letsencrypt.org/) is my suggestion.

## Examples

```
docker run -d --name=phmeter -p 1883:1883 -p 8883:8883 -p 3000:3000 \
    -v phdata:/var/lib/influxdb \
    -e "GF_SECURITY_ADMIN_PASSWORD=<grafana-admin-password>" \
    -e "MOSQ_PHMETER_PASS=<your-phmeter-password>" \
    -e "MOSQ_USER_PASS=<your-user-password>" \
    -e "GF_AUTH_ANONYMOUS_ENABLED=true" \
    zappka/phmeter
```
This starts a container with the name "phmeter" with a Grafana accessible without login on http://localhost:3000 and accepts mqtt via port 1883.