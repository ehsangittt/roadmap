import requests

selectedRegion = input("Enter the region name you want to turn on/off ...\n")

headers = {
    'Authorization': 'Apikey bc26b2d6-e2f5-55ca-8be7-27fecb44a5a4'
}
url = "https://napi.arvancloud.ir/ecc/v1/regions/"+selectedRegion+"/servers"

resp = requests.get(url, headers=headers)

serverID = resp.json().get("data")[0].get("id")

selectedAction = input("Choose on/off ...\n")

powerOnUrl = "https://napi.arvancloud.ir/ecc/v1/regions/"+selectedRegion+"/servers/"+serverID+"/power-"+selectedAction

response = requests.post(powerOnUrl, headers=headers)

print(response.json().get("message"))
