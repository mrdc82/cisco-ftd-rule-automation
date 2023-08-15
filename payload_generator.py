
'''
Python program to update json file
PortLiteral Mappings
--------------------
tcp: 6
udp: 17
icmp: protocol = 1 , "icmpType": "Any"
'''

import json
import extract_change_values
import itertools
from extract_change_values import file, fileselect
import os
import re
import tkinter.filedialog as fd

#remove .txt. from file name
chgfile = fileselect.rstrip('.txt')
print(chgfile)

#ask where to save files to
saveto = fd.askdirectory(title='Save files to directory')

#create payload template and import into new file
with open('payload.json','r') as original, open(f'{chgfile}.json','w') as newfile:
	newfile.write(original.read())

# function to add to JSON
def write_source_json(new_data, filename=f'{newfile.name}'):
	with open(filename,'r+') as file:
		# First we load existing data into a dict.
		file_data = json.load(file)
		# Join new_data with file_data inside emp_details
		file_data["sourceNetworks"]["literals"].append(new_data)
		# Sets file's current position at offset.
		file.seek(0)
		# convert back to json.
		json.dump(file_data, file, indent = 4)

def write_dest_json(new_data, filename=f'{newfile.name}'):
	with open(filename,'r+') as file:
		# First we load existing data into a dict.
		file_data = json.load(file)
		# Join new_data with file_data inside emp_details
		file_data["destinationNetworks"]["literals"].append(new_data)
		# Sets file's current position at offset.
		file.seek(0)
		# convert back to json.
		json.dump(file_data, file, indent = 4)

def write_port_json(new_data, filename=f'{newfile.name}'):
	with open(filename,'r+') as file:
		# First we load existing data into a dict.
		file_data = json.load(file)
		# Join new_data with file_data inside emp_details
		file_data["destinationPorts"]["literals"].append(new_data)
		# Sets file's current position at offset.
		file.seek(0)
		# convert back to json.
		json.dump(file_data, file, indent = 4)

	# python object to be appended
    # iterate through list of ip's
sourceip = extract_change_values.sourceip
destip = extract_change_values.destip
dstport = extract_change_values.destport
portliterals = {"tcp":6,"udp":17,"icmp":1}  #this is a static dictionary to refer to when building payload

for src in sourceip:
    s = {"type":"Host",
        "value": src
        }
    write_source_json(s)

for dst in destip:
    d = {"type":"Host",
        "value": dst
        }
    write_dest_json(d)

#iterate through dictionary and populate list
port_list = [[k,v] for k, values in dstport.items() for v in values]
#remove duplicate lists from list
port_list.sort()
port_list = list(port_list for port_list,_ in itertools.groupby(port_list))

for dp in port_list:
    if dp[0] == "udp":
        pl = portliterals["udp"]
        dport = dp[1]
        ptype = "PortLiteral"
        
        p = {"type": ptype,
        "port": dport,
        "protocol": pl
		}
        write_port_json(p)

    elif dp[0] == "tcp":
        pl = portliterals["tcp"]
        dport = dp[1]
        ptype = "PortLiteral"
        
        p = {"type": ptype,
        "port": dport,
        "protocol": pl
		}
        write_port_json(p)

    elif dp[0] == "icmp":
        ping = {"type":"ICMPv4PortLiteral",
			"protocol": "1",
			"icmpType": "Any"}
        write_port_json(ping)

