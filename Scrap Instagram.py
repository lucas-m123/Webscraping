# -----IMPORTS----- #
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import os
import wget

# -----WEBDRIVER----- #
ruta_driver = "C:/Users/John Salchichón/Desktop/Práctica/Python/chromedriver.exe"
ruta_brave = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
wbop = webdriver.ChromeOptions()
wbop.binary_location = ruta_brave

nav = webdriver.Chrome(executable_path=ruta_driver, chrome_options=wbop)

nav.get("https://instagram.com/")