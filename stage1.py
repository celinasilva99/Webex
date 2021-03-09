import requests
import json
from env import config

baseurl = 'https://webexapis.com/v1/rooms'
token = "enter token here"

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
    'text': 'Hi, Welcome'
}

mess_response = requests.post(
    mess_url, headers=headers, data=json.dumps(mess_body)).json()

memberships = 'https://webexapis.com/v1/memberships'

memb_body = {
    'roomId': roomId,
    'personEmail': 'user@company.com',
    'isModerator': False
}

memberships_response = requests.post(
    memberships, headers=headers, data=json.dumps(memb_body)).json()
