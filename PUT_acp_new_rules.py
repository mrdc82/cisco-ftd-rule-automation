'''
Author: Dino Charalambous
Description: Partially update FTD rules, where Inspection is disabled on the rule.
PortLiteral Mappings
tcp: 6
udp: 17
icmp: protocol = 1 , "icmpType": "Any"
'''

import requests
import json
from generate_token import token
#from payload_generator import chgfile, newfile
import tkinter.filedialog as fd
from pathlib import Path

payloadfile = fd.askopenfilename(title="Select the payload file to load")
p = payloadfile.split('/')
p = p[-1]
chgfile = p.rstrip('.json')
fullname = chgfile.split('_')
rulename = fullname[1]
polid = fullname[0]
fmcip = ""  #put your fmc ip here

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'X-auth-access-token': token
    }

policy_dict = {'ftd_name':'ftd id'}

def blankrule(): #this function creates a blank rule, a partial rule update function will execute after this function.
    global ruleid
    url = f"https://{fmcip}/api/fmc_config/v1/domain/<domain_id>/policy/accesspolicies/{policy_dict[polid]}/accessrules"

    payload = json.dumps({
            "action": "ALLOW",
            "enabled": True,
            "name": rulename,
            "type": "AccessRule",
            "enableSyslog": True,
            "sendEventsToFMC": True,
            "logBegin": False,
            "logEnd": True,
            "newComments": [
                "step 1 create new rule"
            ]})
    
    response = requests.request("PUT", url, headers=headers, data=payload, verify=False)
    response = response.content.decode('utf-8')
    data = json.loads(response)
    jsondata = json.dumps(data, indent=4)
    ruleid = data['id']
    print(ruleid)

def updaterule(): #this function will partial update the newly created rule with the required information.

    url = f"https://{fmcip}/api/fmc_config/v1/domain/<domain_id>/policy/accesspolicies/{policy_dict[polid]}/accessrules/{ruleid}?partialUpdate=true"

    with open(f'{payloadfile}', 'r+', encoding='utf-8') as json_file:
        rule_list = json.load(json_file)
        rule_list['id'] = ruleid
        json_file.seek(0)
        json.dump(rule_list, json_file, indent=4) 
    with open(f'{payloadfile}') as pload:
        pl = json.load(pload)
        payload = json.dumps(pl)   

    response = requests.request("PUT", url, headers=headers, data=payload, verify=False)
    print(response.text)

blankrule()
updaterule()
input("Rule load complete, Press Enter to exit.")
