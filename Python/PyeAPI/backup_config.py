import yaml
import pyeapi
import pprint
import os

pyeapi.load_config('eapi.conf')

file = open('switches.yml', 'r')
switches_dict = yaml.safe_load(file)

exists = os.path.isdir('/home/coder/project/labfiles/V2_L5-CodeRepo/Python/PyeAPI/config_backup')
if not exists:
    os.mkdir('/home/coder/project/labfiles/V2_L5-CodeRepo/Python/PyeAPI/config_backup')

for switch in switches_dict['switches']:
    connect = pyeapi.connect_to(switch)
    device_config = connect.get_config(as_string=True)
    path = '/home/coder/project/labfiles/V2_L5-CodeRepo/Python/PyeAPI/config_backup/'+switch+'_running_config.cfg'
    file = open(path, 'w')
    file.write(device_config)
    file.close()
    print(f"Backing up {switch} config")
