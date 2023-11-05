import requests


url = 'https://assets.breatheco.de/apis/fake/sample/post.php'
headers = {'Content-Type': 'application/json'}
data = {"message": "Este es un mensaje de ejemplo para la solicitud POST"}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    print(response.text)
else:
    print("Error en la solicitud POST")
