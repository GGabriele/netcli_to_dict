import json
import re

with open('show_ip_interface_brief.txt', 'r') as f:
    node_diagram = {}
    results = f.read()
    interface_split = results.split('\n')
    prova = interface_split[2::]
    interface_info = {}
    for line in prova:
        if len(line) > 5:
            interface = {}
            splitted_line = line.split()
            interface['ip address'] = splitted_line[1]
            interface['method'] = splitted_line[3]
            interface['status'] = splitted_line[4]
            if len(splitted_line) > 6:
                interface['status'] = splitted_line[4] + ' ' + splitted_line[5]
                interface['protocol'] = splitted_line[6]
            else:
                    interface['protocol'] = splitted_line[5]
            interface_info[splitted_line[0]] = interface
            node_diagram["interfaces"] = interface_info

print(json.dumps(node_diagram, sort_keys=True, indent=2))
