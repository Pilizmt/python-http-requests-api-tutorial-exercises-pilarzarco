# import requests

# resp = requests.post("https://assets.breatheco.de/apis/fake/sample/save-project-json.php")
# print(resp.text)


import requests
import json

url = 'https://assets.breatheco.de/apis/fake/sample/save-project-json.php'
headers = {'Content-Type': 'application/json'}
data = {
    "id": 2323,
    "title": "Very big project"
}

response = requests.post(url, data=json.dumps(data), headers=headers)

if response.status_code == 200:
    print(response.text)
else:
    print("Error en la solicitud POST")
