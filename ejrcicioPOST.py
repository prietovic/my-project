import requests

body = {
    'a': '1',
    'b': '1',
}

response = requests.post("https://prietovic.pythonanywhere.com//suma_post/",json=body)

print(response.text)

assert response.json()['resultado'] == 2