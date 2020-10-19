import requests

url = 'http://wttr.in/Volgograd?0T'

response = requests.get(url)

print(response.text)