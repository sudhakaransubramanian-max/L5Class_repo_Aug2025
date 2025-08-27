import yaml
import pyeapi
import pprint

pyeapi.load_config('eapi.conf')

file = open('switches.yml', 'r')
devices_dict = yaml.safe_load(file)

for leaf in devices_dict['switches']['leafs']:
    connect = pyeapi.connect_to(leaf)
    vlan_output = connect.enable('show vlan')
    
    print(f"Vlan information for {leaf}")
    for vlan in vlan_output[0]['result']['vlans']:
        
        vlan_name = vlan_output[0]['result']['vlans'][vlan]['name']
        interfaces = []
        for intf in vlan_output[0]['result']['vlans'][vlan]['interfaces']:
            interfaces.append(intf)
        if interfaces:
            print(f"{leaf} has vlan {vlan} with name {vlan_name} with following interfaces assgined {interfaces}")
        else:
            print(f"{leaf} has vlan {vlan} with name {vlan_name} with no interfaces assigned to the vlan")
            
        