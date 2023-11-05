import requests

import requests

url = 'https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # Accede a la primera publicación en la lista
    first_post = data[0]
    author_name = first_post['author']
    print(author_name)
else:
    print("Something went wrong")
