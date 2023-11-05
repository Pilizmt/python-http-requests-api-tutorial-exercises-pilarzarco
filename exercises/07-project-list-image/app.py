import requests

url = 'https://assets.breatheco.de/apis/fake/sample/project_list.php'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # Accede al último proyecto en la lista
    last_project = data[-1]
    # Accede a la última imagen en el proyecto
    last_image_url = last_project['images'][-1]
    print(last_image_url)
else:
    print("Something went wrong")
