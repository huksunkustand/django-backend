import time
import ssl
import os
import json
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from core.utils import DiccionarioPalabrasDelictivas

load_dotenv()

def getAnalisisPost(self,profile):
    FACEBOOK_USER = os.getenv("FACEBOOK_USER")
    FACEBOOK_PASSWORD = os.getenv("FACEBOOK_PASSWORD")

    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)

    #####background
    chromeOptions = Options()
    chromeOptions.headless = True
    ##########

    # driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe', chrome_options=chrome_options)
    driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe', options=chromeOptions)
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
    password.send_keys(FACEBOOK_PASSWORD)
    login = driver.find_element("css selector", "button[type='submit']").click()


    time.sleep(3)
    images = [] 

    driver.get("https://www.facebook.com/"+profile+"/")
    time.sleep(3)
        
    for j in range(0,2):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

    anchors = driver.find_elements("tag name", "a")
    anchors = [a.get_attribute('href') for a in anchors]
    anchors = [a for a in anchors if str(a).startswith("https://www.facebook.com/"+profile+"/posts")]
    # print(anchors)
    keyWords =  DiccionarioPalabrasDelictivas()
    arrayData = []
    for post in anchors:
        driver.get(post)
        time.sleep(2)
        texto=driver.find_element(By.XPATH,'//div')
        #texto= driver.find_element(By.XPATH,"//div[contains(@class,'xkhd6sd x1g2khh7 x4uap5 xyinxu5')]") if driver.find_element(By.XPATH,"//div[contains(@class,'xkhd6sd x1g2khh7 x4uap5 xyinxu5')]") != '' else ''
        texto=texto.text
        # print(texto)
        palabraEcontrada = ''
        for item in keyWords:    
            if item.lower() in texto.lower(): 
                palabraEcontrada = item
        arrayData.append({'urlpost': post, 'publicacion': texto , 'palabraEcontrada': palabraEcontrada})
    return(arrayData)


