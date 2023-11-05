import requests

def get_post_tags(post_id):
    # your code here
    url = 'https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        for post in data:
            if post['id'] == post_id:
                return post['tags']
        # Si no se encuentra el post con el ID especificado, retornar una lista vacía
        return []

    # Si la solicitud no se completa correctamente, también retornar una lista vacía
    return []

# Define el ID del post que deseas buscar
post_id = 146  # Cambia esto al ID del post que deseas buscar

tags = get_post_tags(post_id)
print(tags)
    # return None


print(get_post_tags(146))