import requests
import streamlit as st
import datetime
from wordOfTheDay import sendWord, sendQuote

st.title('Quotivate')

name = st.text_input('Name')
phone_number = st.text_input('Phone Number')

if st.button('Sign me up for Word of the Day'):
    if name and phone_number:
        data = {'Name': name, 'Phone Number': phone_number}
        service_name = 'word_of_day'
        response = requests.post(f'http://localhost:5000/add-user/{service_name}', json=data)
        if response.ok:
            st.success('User added successfully')
        else:
            st.error('Failed to add user')
    else:
        st.warning('Please enter a name and phone number')

if st.button('Sign me up for Quote of the Day'):
    if name and phone_number:
        data = {'Name': name, 'Phone Number': phone_number}
        service_name = 'quote_of_day'
        response = requests.post(f'http://localhost:5000/add-user/{service_name}', json=data)
        if response.ok:
            st.success('User added successfully')
        else:
            st.error('Failed to add user')
    else:
        st.warning('Please enter a name and phone number')

# Get users for Word of the Day service
response_word = requests.get('http://localhost:5000/get-users/word_of_day')
if response_word.ok:
    users_word = response_word.json() # is a list of jsons

# Get users for Quote of the Day service
response_quote = requests.get('http://localhost:5000/get-users/quote_of_day')
if response_quote.ok:
    users_quote = response_quote.json() # is a list of jsons

now = datetime.datetime.now()
eight_am = datetime.datetime.now().replace(hour=8, minute=0, second=0, microsecond=0)

if now == eight_am:
    sendWord(users_word)
    sendQuote(users_quote)

#make a method to send a message to all users
#make a method to send a message to a specific user
def send_message_to_all_users(users, message):
    for user in users:
        name = user['name']
        phone_number = user['phone_number']
        send_message(name, phone_number, message)