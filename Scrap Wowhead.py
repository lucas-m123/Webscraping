# -----IMPORTS----- #
import urllib.request
import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd

# -----FUNCIONES----- #
# Wowhead muestra en primera linea algunas noticias destacadas (son 6 hasta el día de la fecha), por
# lo que esta función sirve, de manera simple, para revertir el orden, tomar las primeras 20 noticias
# (que son las principales que queremos en nuestro .csv) y volvera revertir para filtrar esas primeras 6
# noticias destacadas.
def reversa(a):
    a.reverse()
    del a[20:]
    a.reverse()

# -----URL, STATUS_CODE, SOUP----- #
# Indicarle al request qué página queremos abrir.
url = "https://wowhead.com"
pagina = urllib.request.urlopen(url)
soup = bs(pagina, "html.parser")
# r = requests.get(url)
# print(r.status_code)

# -----ITERACIÓN DE TÍTULOS----- #
# Toma todos los títulos con la etiqueta h2 del DOM.
nombres = soup.body.findAll("h2")
array_nombres = []
for nombre in nombres:
    nombre = nombre.text
    array_nombres.append(nombre)
reversa(array_nombres)
# print(array_nombres)
# print(len(array_nombres))

# -----ITERACIÓN DE DESCRIPCIONES----- #
# Toma todas las descripciones encasilladas, dentro de los div, con la etiqueta "class" definida abajo.
descripciones = soup.body.findAll("div", attrs={"class": "news-list-card-content"})
array_desc = []
for desc in descripciones:
    desc = desc.text
    desc = desc.replace("\n", "")
    array_desc.append(desc)
reversa(array_desc)
# print(array_desc)
# print(len(array_desc))

# -----ITERACIÓN DE DATOS (LINKS)----- #
# Toma todas las descripciones encasilladas, dentro de los links, con la etiqueta "class" definida abajo.
links = soup.body.findAll("a", attrs={"class": "news-list-card-teaser-image"})
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
# Crea un archivo .csv tomando los tres arrays creados previamente (nombres, descripciones y links)
datos = pd.DataFrame({"Posts:": array_nombres, "Descripción:": array_desc, "Links:": array_links})
datos.index += 1
datos.to_csv("wowhead.csv")
