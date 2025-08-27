import yaml
import pyeapi
import pprint

pyeapi.load_config('eapi.conf')

file = open('vlans.yml', 'r')
vlans_dict = yaml.safe_load(file)

for switch in vlans_dict['switches']:
    connect = pyeapi.connect_to(switch)
    print(f"Connecting to Switch {switch}")
    vlan_inst = connect.api('vlans')
    for vlan in vlans_dict['vlans']:
        vlan_id = vlan['id']
        vlan_name = vlan['name']
        print(f"Adding vlan {vlan_id} to Switch {switch}")
        vlan_inst.create(vlan_id)
        vlan_inst.set_name(vlan_id, vlan_name)

