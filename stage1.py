import requests
import json
from env import config

baseurl = 'https://webexapis.com/v1/rooms'
token = "NTdhMmZiYWEtZjIyNy00ZjVmLTkyMTYtNzJjMmRiOTM1NmE0MDk2YjY3YjgtNDcx_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"

headers = {'Authorization': f"Bearer {token}",
           'Content-Type': 'application/json'}

body = {
    "title": "Celina room"
}
post_response = requests.post(
    baseurl, headers=headers, data=json.dumps(body)).json()


response = requests.get(baseurl, headers=headers).json()
rooms = response['items']
for room in rooms:
    if room['title'] == 'Celina room':
        roomId = room['id']
        print(room['title'], roomId)

mess_url = 'https://webexapis.com/v1/messages'

mess_body = {
    'roomId': roomId,
    'text': 'Hi, Welcome to Celinas Space'
}

mess_response = requests.post(
    mess_url, headers=headers, data=json.dumps(mess_body)).json()

memberships = 'https://webexapis.com/v1/memberships'

memb_body = {
    'roomId': roomId,
    'personEmail': 'andrusu@cisco.com',
    'isModerator': False
}

memberships_response = requests.post(
    memberships, headers=headers, data=json.dumps(memb_body)).json()
