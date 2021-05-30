# -----IMPORTS----- #
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
import wget

# -----WEBDRIVER----- #
ruta_driver = "C:/Users/John Salchichón/Desktop/Práctica/Python/chromedriver.exe"
# Las lineas 15 y 16 son para usar el navegador en modo incógnito, no son obligatorias
incognito = webdriver.ChromeOptions()
incognito.add_argument("--incognito")
nav = webdriver.Chrome(executable_path=ruta_driver, options=incognito)
nav.get("https://instagram.com/")

# -----INGRESAR CUENTA DE INSTAGRAM----- #
usuario = WebDriverWait(nav, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "input[name=username]")))
contraseña = WebDriverWait(nav, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "input[name=password]")))
usuario.clear()
contraseña.clear()
usuario.send_keys("") # Tu nombre de usuario de Instagram
contraseña.send_keys("") # Tu contraseña de Instagram
ingresar = WebDriverWait(nav, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button[type=submit]"))).click()
# Probablemente tengas que correr la linea 30 dos veces, dependiendo de la cantidad de pop ups que tengas
ahora_no = WebDriverWait(nav, 10).until(ec.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Ahora no')]"))).click()

# -----INGRESAR A LA BARRA DE BÚSQUEDA----- #
# La linea 35 tiene que estar contemplada porque, al menos en mi caso, Instagram no muestra la barra de búsqueda
# por default, sino que primero hay que clickearla para que se muestre y recién ahí ingresar el texto
click_busqueda = WebDriverWait(nav, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "span[class='TqC_a']"))).click()
busqueda = WebDriverWait(nav, 10).until(ec.element_to_be_clickable((By.XPATH, "//input[@placeholder='Buscar']")))
busqueda.clear()
nombre = "" # El nombre del Instagram o del hashtag que quieras buscar
busqueda.send_keys(nombre)
time.sleep(1)
busqueda.send_keys(Keys.ENTER)
time.sleep(1)
busqueda.send_keys(Keys.ENTER)

# -----RECORRER LA PÁGINA DE INSTAGRAM INGRESADA----- #
# Probablemente tengas que repetir el scroll de la página varias veces más, dado que Instagram va cargando las
# imágenes conforme nosotros vamos haciendo scroll en la página
def scroll():
    time.sleep(2)
    nav.execute_script("window.scrollTo(0,8550);")

for i in range(5):
    scroll()

imagenes = nav.find_elements_by_tag_name("img")
imagenes = [i.get_attribute("src") for i in imagenes]

# -----DESCARGAR LAS IMÁGENES----- #
# Usa el nombre del término de búsqueda para nombrar la carpeta de origen y las fotos descargadas
time.sleep(3)
ruta = os.getcwd()
ruta = os.path.join(ruta, nombre + " fotos")
os.mkdir(ruta)

n = 1
for i in imagenes:
    guardar = os.path.join(ruta, nombre + str(n) + ".jpg")
    wget.download(i, guardar)
    n += 1