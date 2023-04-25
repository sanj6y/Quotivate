import json
from trycourier import Courier
import requests

# create an instance of the Client class
client = Courier(auth_token='Y2RmM2VhMjQtZGY5ZC00NGM3LWI3ZWEtOWQwN2NlOGJlOTk2', username='Github_74223798', base_url='https://api.courier.com')

# list of jsons
json_list = [
    {
        "id": 1,
        "name": "Sanjay",
        "phone_number": "408 391 9768"
    },
    # add more jsons here
]

# iterate over each entry in the list of jsons
for json_entry in json_list:
    url = "https://www.dictionaryapi.com/api/v3/references/collegiate/json/"
    params = {
        "key": "7b6d3174-ca54-45b7-b664-641e2c3d2c8f",
        "date": "today"
    }
    response = requests.get(url, params=params)
    print(response)
    word_of_the_day = response.json()[0]["meta"]["id"]
    
    # create a message using the json entry and the word of the day
    message = {
        "recipient": json_entry["phone_number"],
        "profile": {
            "id": json_entry["id"],
            "name": json_entry["name"]
        },
        "data": {
            "word_of_the_day": word_of_the_day
        }
    }
    
    # send the message using the send method of the Client class
    response = client.send(
        event="WORD_OF_THE_DAY",
        recipient=json_entry["phone_number"],
        profile={
            "id": json_entry["id"],
            "name": json_entry["name"]
        },
        data={
            "word_of_the_day": word_of_the_day
        }
    )
    
    # print the response to the console
    print(response)
