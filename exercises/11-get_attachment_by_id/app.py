import requests

def get_attachment_by_id(attachment_id):
    # your code here
    url = 'https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        for post in data:
            attachments = post.get('attachments', [])
            for attachment in attachments:
                if attachment.get('attach_id') == attachment_id:
                    return attachment.get('title', None)
    
    # Si no se encuentra el adjunto con el ID especificado, retornar None
    return None

# Define el ID del adjunto que deseas buscar
attachment_id = 137  # Cambia esto al ID del adjunto que deseas buscar

attachment_title = get_attachment_by_id(attachment_id)
if attachment_title is not None:
    print(attachment_title)
else:
    print("Attachment not found.")
    # return None

print(get_attachment_by_id(137))