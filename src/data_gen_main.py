from sys_data_gen import SystemDataGenerator
from utils import get_config

if __name__ == '__main__':
    system_list = []
    cfg = get_config(config_path='/home/training/git/data_gen/config')
    # Create all systems from config
    # and initiate metrics for each
    print('Creating systems...')
    for sys in cfg:
        curr_sys = SystemDataGenerator(sys)
        curr_sys.set_metrics_from_config(config_path='/home/training/git/data_gen/config')
        system_list.append(curr_sys)

    # generate records for all systems
    print(f'Creating records...')
    records = []
    for system in system_list:
        records.append(system.generate_record())

    print(records)