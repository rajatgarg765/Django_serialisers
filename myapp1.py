import requests
import json

url ="http://127.0.0.1:8000/stucreate/"

data={
    "id":91,
    "name":"Shushant",
    "roll":104,
    "city":"Allahabad"
}

json_data=json.dumps(data)

r=requests.post(url=url,data=json_data)

data=r.json()

print(data)