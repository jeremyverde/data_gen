from kafka import KafkaConsumer
from json import loads, dumps

class DataConsumer:
    def __init__(self):
        self.consumer = KafkaConsumer('sys_data', bootstrap_servers=['kafka-1:9092','kafka2:9092','kafka-3:9092'],
                            api_version=(2,5,0))

    def bytes_to_json(self, bytes_msg):
        json_str = bytes_msg.decode('utf8').replace("'", '"')
        data = loads(json_str)
        return data
 
    def consume(self):
        for msg in self.consumer:
            print('got a message: ')
            # print(msg.value)
            value_b = msg.value
            data = self.bytes_to_json(value_b)
            yield data

    def close(self):
        self.consumer.close()


if __name__ == "__main__":
    consumer = DataConsumer()
    for anom in consumer.consume():
        print('yielded anomaly')
    
