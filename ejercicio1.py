import requests
import json

param1 = '1'
param2 = '2'


url = "https://ammtp.pythonanywhere.com/testapp/get_example"
parametros = {
    'param1': '1',
    'param2': '2',
 }
response = requests.get(url, params=parametros)

print('STATUS:  ', response.status_code)
print('RESPONSE:', response.text)  # json
data = response.json()  # equivale a: json.loads(response.text)

valor1 = data['request']['params']['param1']
valor2 = data['request']['params']['param2']


assert valor1 == param1
assert valor2 == param2