#! /usr/bin/python3

import zabbix_requests as zr
import requests
import json

def main():
    # Variables used for access to API
    api_url = ''
    api_login = ''
    api_pass = ''

    # Variable used in requests
    ctype = {'Content-type':'application/json-rpc'}

    # Creating auth key for later requests
    r = requests.post(api_url,zr.auth_req(api_login,api_pass),headers=ctype)
    content = json.loads(r.content)
    auth = content['result']
    
    # Creating host list for dnc
    r = requests.post(api_url,zr.host_list_req(auth),headers=ctype)
    content = json.loads(r.content)
    tmp_host_list = content['result']

    # Loop for updating visible names of hosts included in dnc group with dnc tag
    for host in tmp_host_list:
        r = requests.post(api_url,zr.new_name_get(auth,host['hostid']),headers=ctype)
        content = json.loads(r.content)
        name = content['result'][0]['lastvalue']
        r = requests.post(api_url,zr.update_name(auth,host['hostid'],name),headers=ctype)
        content = json.loads(r.content)

if __name__ == '__main__':
    main()
