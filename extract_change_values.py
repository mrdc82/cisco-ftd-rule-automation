'''
Extract values from change order to be consumed by payload generator
'''

#import requests
#import json
#import os
#import re
import tkinter.filedialog as fd
from netaddr import IPAddress

fileselect = fd.askopenfilename(title="Select a file to load")

sourceip = []
destip = []
destport = {"tcp":[],"udp":[],"icmp":[]}

#read changefile
with open(f"{fileselect}","r") as file:
    try:
        for line in file:
            line = line.split(" ")
            pname = line[0].strip("]")

            src_cidr = str(IPAddress(line[7]).netmask_bits())
            src_ip_mask = line[6]+'/'+src_cidr
            sourceip.append(src_ip_mask)

            dst_cidr = str(IPAddress(line[9]).netmask_bits())
            dst_ip_mask = line[8]+'/'+dst_cidr
            destip.append(dst_ip_mask)

            portproto = line[5].lower()
            destport[portproto] += [line[11]]
    except IndexError:
        print("End of file")

print(sourceip)
print(destip)
print(destport)
