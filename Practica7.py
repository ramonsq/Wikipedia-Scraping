import requests
from bs4 import BeautifulSoup
import json

# Loads HTML into soup
url = " https://en.wikipedia.org/wiki/Comillas_Pontifical_University" 
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

target_tables = soup.find_all("table" , class_="infobox vcard" )
target_table = target_tables[0]
# Si hubiera habido más de una pondriamos del 0 al que hubiese

#BC

# Loads HTML into soup.
url = "https://en.wikipedia.org/wiki/Comillas_Pontifical_University"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
# Locates target table with usefull info.
target_tables = soup.find_all("table", class_="infobox vcard")
target_table = target_tables[0]


data = {}
for tr in target_table.find_all("tr"):
    if tr.find("th"):
        data[tr.find("th").get_text()] = tr.find("td").get_text()    
    if tr.find("a", class_ = "image"):
        data[tr.find("td").get_text()] = tr.find("a", class_ = "image").get("href")


def save_json(path, data):
    with open(path, 'w') as outfile:
        json.dump(data, outfile)

save_json('Practica7.json',data)
