import unittest
from sys_data_gen import SystemDataGenerator
from metric import Metric


class SysGenTester(unittest.TestCase):
    def setUp(self) -> None:
        self.config_dir = 'C:/users/jerem/PycharmProjects/data_gen/config'
        self.config_file = 'sys_config.yaml'

    def test_set_metrics(self):
        pass

    def test_generate_random(self):
        pass

    def test_generate_normal(self):
        sys = SystemDataGenerator(name='test00')
        metric_vals = {'name': 'cpu_busy',
                  'min_val': 0,
                  'max_val': 10,
                  'mean': 10,
                  'sd': 3}
        metric = Metric(**metric_vals)
        metric_value = sys.generate_metric_value_normal(metric)
        assert metric_value[metric.name] > 0
