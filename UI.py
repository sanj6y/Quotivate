import requests
import streamlit as st

st.title('Add Users')

name = st.text_input('Name')
phone_number = st.text_input('Phone Number')

if st.button('Submit'):
    if name and phone_number:
        data = {'Name': name, 'Phone Number': phone_number}
        response = requests.post('http://localhost:5000/add-user', json=data)
        if response.ok:
            st.success('User added successfully')
        else:
            st.error('Failed to add user')
    else:
        st.warning('Please enter a name and phone number')

if st.button('Get Users'):
    response = requests.get('http://localhost:5000/get-users')
    if response.ok:
        users = response.json() #is a list of jsons

        st.write(users)
    else:
        st.error('Failed to get users')
