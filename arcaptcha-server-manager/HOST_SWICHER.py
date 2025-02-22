import requests
from dotenv import load_dotenv

import os

load_dotenv() 

headers = {
    'Authorization': os.getenv("SECRET_KEY")
}

region1_details = requests.get("https://napi.arvancloud.ir/ecc/v1/regions/ir-thr-ba1/servers", headers=headers)
region2_details = requests.get("https://napi.arvancloud.ir/ecc/v1/regions/ir-thr-fr1/servers", headers=headers)
region3_details = requests.get("https://napi.arvancloud.ir/ecc/v1/regions/eu-west1-a/servers", headers=headers)
region4_details = requests.get("https://napi.arvancloud.ir/ecc/v1/regions/ir-tbz-sh1/servers", headers=headers)
region5_details = requests.get("https://napi.arvancloud.ir/ecc/v1/regions/ir-thr-si1/servers", headers=headers)

regions = [ "ir-thr-ba1" , "ir-thr-fr1" , "eu-west1-a" , "ir-tbz-sh1" , "ir-thr-si1" ] 

for i, region in enumerate(regions): 
    print(f"{i+1}: {region}")

selected_region = int(input("enter the index of the region you want to work with: "))

if selected_region == 1:
	servers = region1_details.json().get("data")
	for i, server in enumerate(servers):
		print(f"{i+1}: {server.get('name')}")
	selected_server = int(input("enter the index of the server you want to work with: "))
	chosen_action = input("choose on/off: ")
	response = requests.post("https://napi.arvancloud.ir/ecc/v1/regions/ir-thr-ba1/servers/"+servers[selected_server-1].get('id')+"/power-"+chosen_action, headers=headers)
	print(response.json().get("message"))

elif selected_region == 2:
        servers = region2_details.json().get("data")
        for i, server in enumerate(servers):
                print(f"{i+1}: {server.get('name')}")
        selected_server = int(input("enter the index of the server you want to work with: "))
        chosen_action = input("choose on/off: ")
        response = requests.post("https://napi.arvancloud.ir/ecc/v1/regions/ir-thr-fr1/servers/"+servers[selected_server-1].get('id')+"/power-"+chosen_action, headers=headers)
        print(response.json().get("message"))

elif selected_region == 3:
        servers = region3_details.json().get("data")
        for i, server in enumerate(servers):
                print(f"{i+1}: {server.get('name')}")
        selected_server = int(input("enter the index of the server you want to work with: "))
        chosen_action = input("choose on/off: ")
        response = requests.post("https://napi.arvancloud.ir/ecc/v1/regions/eu-west1-a/servers/"+servers[selected_server-1].get('id')+"/power-"+chosen_action, headers=headers)
        print(response.json().get("message"))

elif selected_region == 4:
        servers = region4_details.json().get("data")
        for i, server in enumerate(servers):
                print(f"{i+1}: {server.get('name')}")
        selected_server = int(input("enter the index of the server you want to work with: "))
        chosen_action = input("choose on/off: ")
        response = requests.post("https://napi.arvancloud.ir/ecc/v1/regions/ir-tbz-sh1/servers/"+servers[selected_server-1].get('id')+"/power-"+chosen_action, headers=headers)
        print(response.json().get("message"))

elif selected_region == 5:
        servers = region5_details.json().get("data")
        for i, server in enumerate(servers):
                print(f"{i+1}: {server.get('name')}")
        selected_server = int(input("enter the index of the server you want to work with: "))
        chosen_action = input("choose on/off: ")
        response = requests.post("https://napi.arvancloud.ir/ecc/v1/regions/ir-thr-si1/servers/"+servers[selected_server-1].get('id')+"/power-"+chosen_action, headers=headers)
        print(response.json().get("message"))
