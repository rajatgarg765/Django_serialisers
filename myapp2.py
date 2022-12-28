import requests
import json

url="http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    data={}
    if id is not None:
        data={"id":id}
    json_data=json.dumps(data)
    headers={'content-Type':'application/json'}

    r=requests.get(url=url,headers=headers,data=json_data)

    data=r.json()
    print(data)

get_data(2)

def post_data():
    data={"id":4,"name":"Shibhit","roll":104,"city":"Dhanbad"}
    headers={'content-Type':'application/json'}

    json_data=json.dumps(data)
    r=requests.post(url=url,headers=headers,data=json_data)
    data=r.json()
    print(data)

# post_data()

def update_data():
    data={"id":4,"name":"Linter","city":"Guwahati"}
    json_data=json.dumps(data)
    headers={'content-Type':'application/json'}
    r=requests.put(url=url,headers=headers,data=json_data)
    data=r.json()
    print(data)

# update_data()


def delete_data():
    data={"id":7}
    json_data=json.dumps(data)
    headers={'content-Type':'application/json'}
    r=requests.delete(url=url,headers=headers,data=json_data)
    data=r.json()
    print(data)


# delete_data()