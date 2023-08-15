'''
generate token
'''

import requests
import json

url = "https://<fmc_ip>/api/fmc_platform/v1/auth/generatetoken"

payload = {}
headers = {
  'Accept': 'application/json',
  'Authorization': '<your_auth_key>'
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)
token = response.headers['X-auth-access-token']
print(token)