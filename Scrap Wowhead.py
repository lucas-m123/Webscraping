# -----IMPORTS----- #
import urllib.request
import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd

# -----FUNCIONES----- #
def reversa(a):
    a.reverse()
    del a[20:]
    a.reverse()

# -----URL, STATUS_CODE, SOUP----- #
url = "https://wowhead.com"
pagina = urllib.request.urlopen(url)
soup = bs(pagina, "html.parser")
# r = requests.get(url)
# print(r.status_code)

# -----ITERACIÓN DE TÍTULOS----- #
nombres = soup.body.findAll("h1")
array_nombres = []
for nombre in nombres:
    nombre = nombre.text
    array_nombres.append(nombre)
reversa(array_nombres)
# print(array_nombres)
# print(len(array_nombres))

# -----ITERACIÓN DE DESCRIPCIONES----- #
descripciones = soup.body.findAll("div", attrs={"class": "news-post-content"})
array_desc = []
for desc in descripciones:
    desc = desc.text
    desc = desc.replace("\n", "")
    array_desc.append(desc)
reversa(array_desc)
# print(array_desc)
# print(len(array_desc))

# -----ITERACIÓN DE DATOS (LINKS)----- #
links = soup.body.findAll("a", attrs={"class": "news-post-teaser-image"})
array_links = []
for link in links:
    link = link.get("href")
    array_links.append(link)
reversa(array_links)
for i in range(len(array_links)):
    if array_links[i][0:8] != "https://":
        array_links[i] = url + array_links[i]
# print(array_links)
# print(len(array_links))

# -----CREACIÓN DE DATAFRAMES Y CSV----- #
datos = pd.DataFrame({"Posts:": array_nombres, "Descripción:": array_desc, "Links:": array_links})
datos.index += 1
datos.to_csv("wowhead.csv")
