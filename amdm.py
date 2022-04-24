import requests
from bs4 import BeautifulSoup


def text_read():
    with open("config.txt") as file:
        s = file.read()
        return s


def text_clean():
    with open("config.txt", "w") as file:
        return file.write("")  


def text_write(song):
    with open("config.txt", "a") as file:
        return file.write(song)


def x():
    with open("config.txt") as file_old:
        s = file_old.read()
    with open("config.txt", "w") as file_w:
        file_w.write(s[:-1])


def amdm(period="all", first_page=1, last_page=2):

    if last_page > 10:
        last_page = 10
    if first_page < 1:
        first_page = 1

    text_clean()
    
    number = 0
    while first_page != last_page+1:
        response = requests.get(f"https://amdm.ru/akkordi/popular/{period}/page{first_page}/")
        soup = BeautifulSoup(response.content, "lxml")
        data = soup.find('table', {"class": "items"}).findAll(class_="artist_name")
        for curse in data:
            number += 1
            text_write(f"{number }  {curse.text}\n")
        first_page += 1

    x()
    print(text_read())

amdm(input("period (month or all): "), int(input("first_page: ")), int(input("last_page: ")))
