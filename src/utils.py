from yaml import load, SafeLoader
from os import path

def dt_to_str(date_time):
    return date_time.strftime("%m/%d/%Y, %H:%M:%S")


def get_config(config_path=None, config_file=None):
    if config_path is None:
        config_path = 'C:/users/jerem/PycharmProjects/data_gen/config'
    if config_file is None:
        config_file = 'sys_config.yaml'
    config_file_path = path.join(config_path, config_file)
    with open(config_file_path) as file:
        return load(file, SafeLoader)