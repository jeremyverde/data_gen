from metric import Metric
from random import uniform
from datetime import datetime
from time import mktime
from utils import get_config, dt_to_str
from numpy.random import normal


class SystemDataGenerator:
    def __init__(self, name):
        self.name = name
        self.metrics = []

    def set_metrics(self, metric_list):
        for metric in metric_list:
            curr_metric = Metric(**metric)
            self.metrics.append(curr_metric)

    def set_metrics_from_config(self, config_path=None, config_file=None):
        cfg = get_config(config_path, config_file)
        metric_list = cfg[self.name]['metrics']
        self.set_metrics(metric_list)

    def generate_metric_value(self, metric):
        value = uniform(metric.min_val, metric.max_val)
        return {metric.name: value}

    def generate_metric_value_normal(self, metric):
        value = normal(metric.mean, metric.sd, 1)
        return {metric.name: value[0]}

    def generate_all_metrics(self):
        curr_metric_values = {}
        for metric in self.metrics:
            curr_metric_values.update(self.generate_metric_value_normal(metric))

        return curr_metric_values

    def generate_record(self):
        metrics = self.generate_all_metrics()
        time_now = datetime.now()
        time_utc = int(mktime(time_now.timetuple())*1000)        
        metrics.update({'name': self.name, 'time': time_utc})
        return metrics
