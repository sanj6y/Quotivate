import json
from trycourier import Courier
import requests

def sendOne(pn, body):
    api_key = "pk_prod_HF62V1AYE64SNFQTXTF3YE9MRD0F"
    url = "https://api.courier.com/send"
   
    payload = {
        "message": {
            "to": {
                "phone_number": pn,
            },
            "content": {
                "body": body
            }
        }
    }
    
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + api_key 
    }
    
    response = requests.request("POST", url, headers = headers, json = payload)
    return response

def sendWord(json_list):
    for json_entry in json_list:
        response = requests.get("https://api.wordnik.com/v4/words.json/wordOfTheDay?api_key=c86lwn64t3vvmvd0y9qsofjce3ppgrvsvm4q5vwq49wmoadhw")
        word_of_the_day = response.json()["word"]

        definition = response.json()["definitions"][0]["text"]

        message = "Hey " + json_entry["name"] + "!\nYour word of the day is: " + word_of_the_day + ".\nDefinition: " + definition
        
        # create msg
        sendOne(json_entry["phone_number"], message)

def sendQuote(json_list):
    for json_entry in json_list:
        response = requests.get("https://zenquotes.io/api/random")
        quote = json.loads(response.text)
        quote = quote[0]['q'] + " - " + quote[0]['a']
        quote = '"' + quote.split(' -')[0] + '" -' + quote.split(' -')[-1]

        message = "Hey " + json_entry["name"] + "!\nHere's your motivational quote: " + quote
        
        # create msg
        sendOne(json_entry["phone_number"], message)

# json_list = [
#     {
#         "id": 0,
#         "name": "Pranav",
#         "phone_number": "6504395248"
#     }
# ]

json_list = requests.get('http://localhost:5000/get-users').json()


sendWord(json_list)
sendQuote(json_list)