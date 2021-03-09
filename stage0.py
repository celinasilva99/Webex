import requests
import json
from env import config

baseurl = 'https://webexapis.com/v1/rooms'
token = "NTdhMmZiYWEtZjIyNy00ZjVmLTkyMTYtNzJjMmRiOTM1NmE0MDk2YjY3YjgtNDcx_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"

headers = {'Authorization': f"Bearer {token}",
           'Content-Type': 'application/json'}


response = requests.get(url, headers=headers).json()
teams = response['items']
for team in teams:
    if team['title'] == 'Programmability CTF - Day 1 - Team 1':
        teamId = team['id']
        print(team['title'], teamId)
