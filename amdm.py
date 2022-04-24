import requests
from bs4 import BeautifulSoup


def amdm(firt_page=1, last_page=2):
    count = 0
    while firt_page != last_page+1:
        response = requests.get(f"https://amdm.ru/akkordi/popular/all/page{firt_page}/")
        soup = BeautifulSoup(response.content, "lxml")
        data = soup.find('table', {"class": "items"}).findAll(class_="artist_name")
        for curse in data:
            count += 1
            print(count, curse.text)
        firt_page += 1


amdm()
