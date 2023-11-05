import requests

def get_titles():
    # your code here
    url = 'https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        titles = [post['title'] for post in data]
        return titles
    else:
        return []
    
    # return None


print(get_titles())