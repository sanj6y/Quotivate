import requests
import json

response = requests.get("https://zenquotes.io/api/random")
data = json.loads(response.text)

print(data[0]['q'] + " - " + data[0]['a'])
