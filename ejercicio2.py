import requests
import json

url = "https://ammtp.pythonanywhere.com/testapp/post_example"

data='123456789'

response = requests.post(url, data=data)

valor = response.json()['request']['body']

assert valor == '123456789'