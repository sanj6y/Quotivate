import requests
from bs4 import BeautifulSoup

# Send a GET request to the Merriam-Webster word of the day calendar
response = requests.get("https://www.merriam-webster.com/word-of-the-day/calendar")

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, "html.parser")

# Extract the list of word of the day entries
wod_carousel = soup.find_all("div", class_="wod-carousel card-box")


# Extract the words of the day from each entry
words_of_the_day = []
for entry in word_entries:
    date = entry.find("span", class_="wotd-item-date").text.strip()
    word = entry.find("h1", class_="hword").text.strip()
    words_of_the_day.append((date, word))

# Print the list of words of the day
for date, word in words_of_the_day:
    print(date + ": " + word)
