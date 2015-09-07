#!/usr/bin/env python

import re
import json

with open('show_port-channel_summary.txt', 'r') as f:
    port_channel_facts = []
    
    for line in f:
        if re.search(".*Et\d", line):
            for ether_channel in line.split():
                if ether_channel.startswith("Po"):
                    port_channel = {}
                    port_channel_interfaces = []
                    port_channel['port_channel_name'] = ether_channel.split('(')[0]
                if ether_channel.startswith("LACP"):
                    port_channel['protocol'] = ether_channel.split('(')[0]
                if ether_channel.startswith("Et"):
                    port_channel_interfaces.append(ether_channel.split('(')[0])

        try:
            if port_channel not in port_channel_facts:
                port_channel['interfaces'] = port_channel_interfaces
                port_channel_facts.append(port_channel)
        except NameError:
            pass

f.close()

print(json.dumps(port_channel_facts, sort_keys=True, indent=2))
