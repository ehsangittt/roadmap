import requests

regions = [ "ir-thr-ba1" , "ir-thr-fr1" , "eu-west1-a" , "ir-tbz-sh1" , "ir-thr-si1" ]

url = "https://napi.arvancloud.ir/ecc/v1/regions/ir-thr-ba1/servers"

url = "https://napi.arvancloud.ir/ecc/v1/regions/eu-west1-a/servers"

url = "https://napi.arvancloud.ir/ecc/v1/regions/ir-thr-fr1/servers"

url = "https://napi.arvancloud.ir/ecc/v1/regions/ir-tbz-sh1/servers"

url = "https://napi.arvancloud.ir/ecc/v1/regions/ir-thr-si1/servers"


selectedRegion = input("Enter the region name you want to turn on/off ...\n")

headers = {
    'Authorization': 'Apikey bc26b2d6-e2f5-55ca-8be7-27fecb44a5a4'
}

resp = requests.get(url, headers=headers)

serverID = resp.json().get("data")[0].get("id")

selectedAction = input("Choose on/off ...\n")

powerOnUrl = "https://napi.arvancloud.ir/ecc/v1/regions/"+selectedRegion+"/servers/"+serverID+"/power-"+selectedAction

response = requests.post(powerOnUrl, headers=headers)

print(response.json().get("message"))
