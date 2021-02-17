from metric import Metric
from random import uniform
from datetime import datetime
from utils import get_config, dt_to_str


class SystemDataGenerator:
    def __init__(self, name):
        self.name = name
        self.metrics = []

    def set_metrics(self, metric_list):
        for metric in metric_list:
            curr_metric = Metric(**metric)
            self.metrics.append(curr_metric)

    def set_metrics_from_config(self, config_path=None, config_file=None):
        cfg = get_config(config_file, config_path)
        metric_list = cfg[self.name]['metrics']
        self.set_metrics(metric_list)

    def generate_metric_value(self, metric):
        # TODO: use better generation, normal dist maybe
        value = uniform(metric.min_val, metric.max_val)
        return {'metric': metric.name, 'value': value}

    def generate_all_metrics(self):
        curr_metric_values = []
        for metric in self.metrics:
            curr_metric_values.append(self.generate_metric_value(metric))

        return curr_metric_values

    def generate_record(self):
        metrics = self.generate_all_metrics()
        time = dt_to_str(datetime.now())
        return {'name': self.name, 'date_time': time, 'metrics': metrics}

