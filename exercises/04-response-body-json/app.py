import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")
print(response.text)


if response.status_code == 200:
    data = response.json()
    current_time = f"Current time: {data['hours']} hrs {data['minutes']} min and {data['seconds']} sec"
    print(current_time)
else:
    print("Something went wrong")