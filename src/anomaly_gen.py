from data_consumer import DataConsumer
from anomaly_producer import AnomalyProducer
from anomaly import Anomaly


def check_anomaly(metric):
        if metric > 50:
            return True
        return False

if __name__ == "__main__":
    consumer = DataConsumer()
    producer = AnomalyProducer()
    topic = 'cpu_anomalies'

    for data in consumer.consume():
        job_id = 'ml_test_cpu__v1'
        metric_raw = 'cpu_busy'

        print('checking for anomalies...')
        print('data: ', data)
        actual = data[metric_raw]
        anom = check_anomaly(actual)
        print(f'Anomalous: {anom}')

        if anom:
            new_anomaly = Anomaly(record=data, job_id=job_id, actual=actual, metric_raw=metric_raw)
            print(f'new anomaly created: {new_anomaly.anomaly_time}')
            new_anomaly
            producer.produce_to_cluster(topic, new_anomaly)