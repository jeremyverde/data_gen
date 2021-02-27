from datetime import datetime
from time import mktime

class Anomaly:
    def __init__(self, record, job_id, actual, metric_raw):
        self.name = record['name']
        self.timestamp = record['time']
        self.job_id = job_id
        self.actual = actual
        self.metric_raw = metric_raw
        self._set_timestamp()
        
    def _set_timestamp(self):
        time_now = datetime.now()
        time_utc = int(mktime(time_now.timetuple())*1000)
        self.anomaly_time = time_utc

