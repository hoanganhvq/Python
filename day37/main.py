import requests
from datetime import datetime
USER_NAME  = "anh"
TOKEN = "abcdefjdfhsdsdf"
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_id = "graph1"
user_params = {
    "token" :TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor":"yes"
}
# respone = requests.post(url=pixela_endpoint, json=user_params)
# print(respone.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
grap_config = {
    "id":"graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers= {
    "X-USER-TOKEN": TOKEN
}
# respone = requests.post(url=graph_endpoint,json=grap_config,headers=headers)
# print(respone.text )

add_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_id}"
today = datetime.now()
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today")
}

# respone = requests.post(url=add_endpoint, json=pixel_data,headers=headers)
# print(respone.text)


update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_id}/{today.strftime("%Y%m%d")}"

update_data ={
    "quantity": "5"
}

# respone = requests.put(url=update_endpoint,json=update_data,headers=headers)
# print(respone.text)

delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_id}/{today.strftime("%Y%m%d")}"
#
# respone = requests.delete(url=delete_endpoint,headers=headers)
#
# print(respone.text)
