import json
from trycourier import Courier
import requests

client = Courier(auth_token='Y2RmM2VhMjQtZGY5ZC00NGM3LWI3ZWEtOWQwN2NlOGJlOTk2', username='sanjay.chandrasekar@gmail.com', base_url='https://api.courier.com')

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

# list of jsons (TEMP)
json_list = [
    {
        "id": 1,
        "name": "Sanjay",
        "phone_number": "4083919768"
    },
    # take input of full list of jsons later
]

def driver(json_list):
    for json_entry in json_list:
        response = requests.get("https://api.wordnik.com/v4/words.json/wordOfTheDay?api_key=c86lwn64t3vvmvd0y9qsofjce3ppgrvsvm4q5vwq49wmoadhw")
        word_of_the_day = response.json()["word"]
        
        # create msg
        sendOne(json_entry["phone_number"], word_of_the_day)