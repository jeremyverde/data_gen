from data_consumer import DataConsumer
from anomaly_producer import AnomalyProducer
from anomaly import Anomaly


from river import compose, linear_model, metrics, preprocessing, anomaly

def init_model():
    # return compose.Pipeline(preprocessing.StandardScaler(),
    #                         linear_model.LogisticRegression())
    # return compose.Pipeline(preprocessing.MinMaxScaler(), anomaly.HalfSpaceTrees(seed=42))
    return anomaly.HalfSpaceTrees(n_trees=5, height=3, window_size=3, seed=42)

    
def apply_update_model(model, metric, record):
    print('hashed name: ', record['V1'])
    score = model.score_one(record)
    # metric = metric.update(y, score)
    model = model.learn_one(record)
    print('score: ', score)
    return score > 0.14, model

def check_anomaly_dummy(metric):
        if metric >= 16:
            return True
        return False

if __name__ == "__main__":
    consumer = DataConsumer()
    producer = AnomalyProducer()
    topic = 'cpu_anomalies'

    model = init_model()
    metric = metrics.ROCAUC()
    
    trained = 0

    try:
        for data in consumer.consume():
            job_id = 'ml_test_cpu__v1'
            metric_raw = 'cpu_busy'

            actual = 1/data[metric_raw]
            time = data['time']
            # chance for divide by zero
            name = 1/(abs(hash(data['name'])) % (10**3))
            record = {'V1': name, 'V2': actual}
            if trained < 6:
                print('training...')
                print({f'trained: {trained}'})
                model = model.learn_one(record)
                trained += 1
            # anom = check_anomaly_dummy(actual)
            else:
                print('checking for anomalies...')
                print('data: ', data)
                anom, model = apply_update_model(model, metric, record)
                print(f'Anomalous: {anom}')

                if anom:
                    new_anomaly = Anomaly(record=data, job_id=job_id, actual=actual, metric_raw=metric_raw)
                    print(f'new anomaly created: {new_anomaly.anomaly_time}')
                    status = producer.produce_to_cluster(topic, new_anomaly)
                    print('status: ', status)

    finally:
        consumer.close()