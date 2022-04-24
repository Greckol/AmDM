import requests
from bs4 import BeautifulSoup


def text_clean():
    with open("config.txt", "w") as file:
        file.write("")


def text(song):
    with open("config.txt", "a") as file:
        file.write(song)


def amdm(firt_page=1, last_page=2):
    text_clean()
    number = 0
    while firt_page != last_page+1:
        response = requests.get(f"https://amdm.ru/akkordi/popular/all/page{firt_page}/")
        soup = BeautifulSoup(response.content, "lxml")
        data = soup.find('table', {"class": "items"}).findAll(class_="artist_name")
        for curse in data:
            number += 1
            text(f"{number }  {curse.text}  \n")
            print(number, curse.text)
        firt_page += 1


amdm(last_page=2)
