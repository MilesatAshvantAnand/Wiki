import requests
from bs4 import BeautifulSoup


# Making a GET request
r = requests.get('https://en.wikipedia.org/wiki/Main_Page')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# Finding by id
s = soup.find('div', id= 'mp-itn')

# Getting the leftbar

# All the li under the above ul
lines = str(s.find_all('li'))

f = open("Content.html", "a")
f.write(lines)
f.close()
