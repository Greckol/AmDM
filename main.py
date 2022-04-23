import requests
from bs4 import BeautifulSoup

i = 1
k = 0
while i != 10:
    response = requests.get(f"https://amdm.ru/akkordi/popular/all/page{i}/")
    soup = BeautifulSoup(response.content, "lxml")
    data = soup.find('table', {"class": "items"}).findAll(class_="artist_name")
    for curse in data:
        k += 1
        print(k, curse.text)
    i += 1


