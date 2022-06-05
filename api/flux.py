# influxdb_client: https://github.com/influxdata/influxdb-client-python
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import configparser
import os
from time import sleep

def wait_for_file(path): # only useful on the first run
    while not os.path.isfile(path):
        sleep(1)

class InfluxAdaptor:
    
    def __init__(self, config_path: str, influx_url: str='http://localhost:8086'):
        self.__bucket = os.getenv('DOCKER_INFLUXDB_INIT_BUCKET')
        org = os.getenv('DOCKER_INFLUXDB_INIT_ORG')
        config = configparser.ConfigParser()
        wait_for_file(config_path)
        config.read(config_path)
        token = config['default']['token'].strip('"')
        client = InfluxDBClient(url=influx_url, token=token, org=org)
        self.write_api = client.write_api(write_options=SYNCHRONOUS)
    
    def write(self, measurement: str, field: str, value: float, bucket: str = None):
        p = Point(measurement).field(field, value)
        self.write_api.write(bucket=bucket or self.__bucket, record=p)
