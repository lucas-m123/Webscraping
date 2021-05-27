# -----IMPORTS-----
import urllib.request
import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd

# -----URL Y STATUS_CODE-----
url = "https://www.wowhead.com/"
pagina = urllib.request.urlopen(url)
# r = requests.get(url)
# print(r.status_code)

# -----DATOS A SCRAPEAR-----
soup = bs(pagina, "html.parser")
nombres = soup.body.findAll("h1")
array_nombres = []
# -----ITERACION DE DATOS (TITULOS)-----
for nombre in nombres:
    nombre = nombre.text
    array_nombres.append(nombre)
array_nombres.reverse()
del array_nombres[20:]
array_nombres.reverse()
# print(array_nombres)
# print(len(array_nombres))

# -----ITERACION DE DATOS (LINKS)-----
# links = soup.find_all("a")
# for link in links:
#     print(link.get("href"))

# -----CREACION DE DATAFRAMES-----
datos = pd.DataFrame({"Posts:": array_nombres})
datos.index += 1
datos.to_csv("wowhead.csv")
