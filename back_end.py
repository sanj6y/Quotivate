
"""
Code structure:
1) Class for actuall disaster notification
    Everytime this file is run we need to the following things:
    1) Make a call to the disaster api and get the events that have occured --> store those in a list called 'events'
    2) Iterate thru the list 'events' and make a query to the db which returns the users number and we store this in a list of tuples as well
        The tuple would be structured as (National Disaster, Name,  Phone Number) ---> call this list 'impacted_users'
    3) Now that we have a list of those who have been impacted we can go through the list of impacted_users
    4) We make a call to the courier api for each user and send them a text message
        Maybe use NLP or something to generate the message? OpenAI API to generate a list of resources?


2) Class for adding and storing users
    This can be done using a sql lite 3 database in python

    This class will have a few methods:
        addUser(): Add a user to the database
        removeUser(): Reomve a user from the database
        getUsers(): return a dataframe which has all of the data from the db

3) Front end:
    Have a gpt powered chatbot that can answer quick questions about any natural disasters that are occuring 
    Integrate a feature in the site where the user can get a realtime list of natural disasters occuring

"""