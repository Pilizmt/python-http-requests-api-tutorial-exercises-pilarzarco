import requests

import requests

url = 'https://assets.breatheco.de/apis/fake/sample/project-1.php'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    project_name = data['name']
    print(project_name)
else:
    print("Something went wrong")
