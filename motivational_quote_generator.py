import requests
import json

response = requests.get("https://zenquotes.io/api/random")
data = json.loads(response.text)

quote = data[0]['q'] + " - " + data[0]['a']

print(quote)

# add quote symbols to quote; quote is in form:
# Talk sense to a fool and he calls you foolish. - Euripides
quote = '"' + quote.split(' -')[0] + '" -' + quote.split(' -')[-1]

print(quote)
