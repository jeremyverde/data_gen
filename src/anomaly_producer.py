from time import sleep, mktime
from datetime import datetime
from json import dumps
from kafka import KafkaProducer
from utils import get_config, dt_to_str
from sys_data_gen import SystemDataGenerator


class AnomalyProducer:
    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers=['kafka-1:9092','kafka2:9092','kafka-3:9092'],
                            api_version=(2,5,0),
                            value_serializer=lambda x: 
                            dumps(x).encode('utf-8'))  

    def produce_to_cluster(self, topic, anomaly):
        # time_now = datetime.now()
        # time_utc = int(mktime(time_now.timetuple())*1000)
        system = anomaly.name
        anom_as_dict = vars(anomaly)
        future = self.producer.send(topic, value=anom_as_dict, key=system.encode('utf-8'))#, timestamp_ms=time_utc)
        result = future.get(timeout=60)
        return result
