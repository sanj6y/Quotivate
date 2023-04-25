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

sendOne("4083919768", "hello world")