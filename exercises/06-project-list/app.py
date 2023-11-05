import requests

import requests

url = 'https://assets.breatheco.de/apis/fake/sample/project_list.php'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # Accede al segundo proyecto en la lista (índice 1 ya que los índices en Python comienzan en 0)
    second_project = data[1]
    project_name = second_project['name']
    print(project_name)
else:
    print("Something went wrong")
