from kafka import KafkaConsumer

if __name__ == "__main__":
    consumer = KafkaConsumer('sys_data')
    for msg in consumer:
        print(msg)