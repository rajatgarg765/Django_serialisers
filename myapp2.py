import requests
import json

url="http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    data={}
    if id is not None:
        data={"id":id}
    json_data=json.dumps(data)

    r=requests.get(url=url,data=json_data)

    data=r.json()
    print(data)

#get_data(2)

def post_data():
    data={"id":213,"name":"Shibhit","roll":2130,"city":"Dhanbad"}
    json_data=json.dumps(data)
    r=requests.post(url=url,data=json_data)
    data=r.json()
    print(data)

post_data()

def update_data():
    data={"id":113,"name":"Linter","city":"Guwahati"}
    json_data=json.dumps(data)
    r=requests.put(url=url,data=json_data)
    data=r.json()
    print(data)

#update_data()


def delete_data():
    data={"id":6}
    json_data=json.dumps(data)
    r=requests.delete(url=url,data=json_data)
    data=r.json()
    print(data)


# delete_data()