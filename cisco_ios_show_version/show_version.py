#!/usr/bin/env python

import json

device_outputs = ['router_show_version.txt', 'switch_show_version.txt']

device_inventory = []

for output in device_outputs:
    with open(output, 'r') as f:
        inventory = {}
        power_serials = []
        for line in f:
            if line.lower().startswith('cisco'):
                if 'IOS' not in line.split()[1]:
                    inventory['model'] = line.split()[1]
            if 'serial number' in line.lower():
                if 'power' not in line.lower():
                    inventory['system_serial'] = line.split()[-1]
                else:
                    power_serials.append(line.split()[-1])
            if 'processor board' in line.lower():
                inventory['system_serial'] = line.split(',')[0].split()[-1]
            if 'system image' in line.lower():
                system_image = line.split()[-1].split(":")[-1].strip("\"")
                inventory['running_image'] = system_image
            if 'configuration register' in line.lower():
                inventory['config_register'] = line.split()[-1]

    if inventory not in device_inventory:
        inventory['power_serial'] = power_serials 
        device_inventory.append(inventory)

    f.close()

print(json.dumps(device_inventory, indent=2, sort_keys=True))
