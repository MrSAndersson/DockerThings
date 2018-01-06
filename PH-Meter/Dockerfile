FROM grafana/grafana

LABEL maintainer="stefan.nigma@gmail.com"
LABEL version="2018.01.06"

# Set timezone in container
ENV TZ=Europe/Stockholm
ENV GF_AUTH_ANONYMOUS_ENABLED=true
ENV GF_DASHBOARDS_JSON_ENABLED=true
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install applications
RUN apt-get update
RUN apt-get install -y apt-transport-https 
RUN curl -sL https://repos.influxdata.com/influxdb.key | apt-key add - source /etc/os-release
RUN echo "deb https://repos.influxdata.com/debian jessie stable" | tee /etc/apt/sources.list.d/influxdb.list
RUN apt-get update
RUN apt-get install -y influxdb mosquitto python3 python3-pip
RUN pip3 install influxdb paho-mqtt

# Copy required files into container
ADD setup.sh /dock/

RUN chmod +x /dock/setup.sh
ADD mosquitto/* /dock/mosquitto/

ADD mqtt_to_influx.py /dock/
RUN chmod +x /dock/mqtt_to_influx.py

ADD grafana/PH-Meter.json /var/lib/grafana/dashboards/

# Clean away unnessecary packages
RUN apt-get remove -y python3-pip apt-transport-https ; apt-get -y autoremove

EXPOSE 1883 3000

ENTRYPOINT [ "/dock/setup.sh" ]