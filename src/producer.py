from time import sleep
from json import dumps
from kafka import KafkaProducer
from utils import get_config
from sys_data_gen import SystemDataGenerator


def produce_to_cluster(emit_producer, topic, data):
    future = emit_producer.send(topic, value=data)
    result = future.get(timeout=60)
    return result

if __name__ == "__main__":
    producer = KafkaProducer(bootstrap_servers=['kafka-1:9092','kafka2:9092','kafka-3:9092'],
                            api_version=(2,5,0),
                            value_serializer=lambda x: 
                            dumps(x).encode('utf-8'))

    system_list = []
    cfg = get_config(config_path='/apps/data/python-producer/data_gen/config')
    # Create all systems from config
    # and initiate metrics for each
    print('Creating systems...')
    for sys in cfg:
        curr_sys = SystemDataGenerator(sys)
        curr_sys.set_metrics_from_config(config_path='/apps/data/python-producer/data_gen/config')
        system_list.append(curr_sys)
    
    while True:
        # generate records for all systems
        print(f'Creating records...')
        records = []
        for system in system_list:
            records.append(system.generate_record())
        status = produce_to_cluster(producer, 'testing', data=records)
        print('send status: ', status)
        sleep(30)
