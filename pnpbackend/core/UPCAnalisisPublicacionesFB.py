import time
import ssl
import os
import json

from selenium.webdriver.common.by import By
from facebook_scraper import get_profile
from urllib.parse import urlparse, parse_qs
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from core.utils import DiccionarioPalabrasDelictivas
load_dotenv()

def getAnalisisPublicacionesFBSelenium(self,nombres,profileId):
    FACEBOOK_USER="985504635"
    FACEBOOK_PASSWORD="Marcelo1609"

    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)

    #####background
    chromeOptions = Options()
    chromeOptions.headless = True
    ##########

    driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe', options=chromeOptions)
    # driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe', chrome_options=chrome_options)

    driver.maximize_window()
    driver.get("https://www.facebook.com/login/")

    ssl._create_default_https_context = ssl._create_unverified_context
    textos = []
    # login
    time.sleep(3)
    username = driver.find_element("css selector", "input[name='email']")
    password = driver.find_element("css selector", "input[name='pass']")
    username.clear()
    password.clear()
    username.send_keys(FACEBOOK_USER)
    time.sleep(3)
    password.send_keys(FACEBOOK_PASSWORD)
    login = driver.find_element("css selector", "button[type='submit']").click()
    time.sleep(5)

    driver.get("https://www.facebook.com/search/posts/?q="+nombres)
    time.sleep(2)
    for j in range(0,3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

    anchors = driver.find_elements("tag name", "a")
    anchors = [a.get_attribute('href') for a in anchors]
    anchors = [a for a in anchors if str(a).startswith("https://www.facebook.com/"+profileId+"/posts")]
    keyWords = DiccionarioPalabrasDelictivas()
    arrayData = []

    for post in anchors:
        driver.get(post)
        time.sleep(2)
        texto=driver.find_element(By.XPATH,'//div')
        texto=texto.text
        #imagenes
        images = driver.find_elements("tag name", "img")
        time.sleep(2)
        images = [image.get_attribute('src') for image in images]

        palabraEcontrada = ''
        for item in keyWords:    
                    if item.lower() in texto.lower():
                        palabraEcontrada = item

        arrayData.append({'Urlphoto': post, 'Publicacion': texto, 'image':images[0],'palabraEcontrada':palabraEcontrada})

    return(arrayData)
