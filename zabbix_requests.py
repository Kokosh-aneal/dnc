#! /usr/bin/python3

import json

#Authentification request
def auth_req(login,password):
    auth = {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": login,
            "password": password
        },
        "id": 1,
        "auth": None
    }
    return json.dumps(auth)

#Request to get list of hosts
def host_list_req(auth):
    req = {
        "jsonrpc":"2.0",
        "method":"host.get",
        "params":{
            "output": [
                "hostid","name"
            ],
            "tags":[
                {
                "tag":"dnc",
                "value":1,
                "operator":0
                }
            ]
        },
        "auth": auth,
        "id": 2
    }
    return json.dumps(req)

def new_name_get(auth,hostid):
    req = {
        "jsonrpc":"2.0",
        "method":"item.get",
        "params":{
            "output":[
                "hostid","lastvalue"
                ],
            "hostids": hostid,
            "search":{
                "key_":"system.name"
                }
            },
        "auth":auth,
        "id":3
    }
    return json.dumps(req)

def update_name(auth,hostid,new_name):
    req = {
        "jsonrpc":"2.0",
        "method":"host.update",
        "params":{
            "hostid":hostid,
            "name": new_name
        },
        "auth":auth,
        "id":1
    }
    return json.dumps(req)


