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
        response = requests.post('http://localhost:5000/add-user', json=data)
        if response.ok:
            st.success('User added successfully')
        else:
            st.error('Failed to add user')
    else:
        st.warning('Please enter a name and phone number')

if st.button('Sign me up for Quote of the Day'):
    if name and phone_number:
        data = {'Name': name, 'Phone Number': phone_number}
        response = requests.post('http://localhost:5000/add-user', json=data)
        if response.ok:
            st.success('User added successfully')
        else:
            st.error('Failed to add user')
    else:
        st.warning('Please enter a name and phone number')

# i want it to be get-word-users and get-quote-users 
response = requests.get('http://localhost:5000/get-users')
if response.ok:
    users = response.json() #is a list of jsons
now = datetime.datetime.now()
eight_am = datetime.datetime.now().replace(hour=8, minute=0, second=0, microsecond=0)

if now == eight_am:
    sendWord(response)
    sendQuote(response)