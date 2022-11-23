import time
import ssl
import os
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
load_dotenv()

def getAnalisisInstagramPerfilSelenium(self,name):
    INSTAGRAM_USER = os.getenv("INSTAGRAM_USER")
    INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")

    #####background
    chromeOptions = Options()
    chromeOptions.headless = True
    ##########

    driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe', options=chromeOptions)
    # driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
    driver.get("https://www.instagram.com/")

    ssl._create_default_https_context = ssl._create_unverified_context

    # login
    time.sleep(4)
    username = driver.find_element("css selector", "input[name='username']")
    password = driver.find_element("css selector", "input[name='password']")
    username.clear()
    password.clear()
    username.send_keys(INSTAGRAM_USER)
    password.send_keys(INSTAGRAM_PASSWORD)
    login = driver.find_element("css selector", "button[type='submit']").click()

    time.sleep(6)
    nothow = driver.find_element(
        "xpath", "//button[contains(text(), 'Ahora no')]").click()
    # turn on notif
    time.sleep(3)
    nothow2 = driver.find_element(
        "xpath", "//button[contains(text(), 'Ahora no')]").click()


    # searchbox
    time.sleep(3)
    searchbox = driver.find_element("css selector", "input[placeholder='Buscar']")
    searchbox.clear()
    searchbox.send_keys(name)
    time.sleep(2)

    #Logica para traer data de los primero 4 perfiles
    arrayData = []
    for publ in range(1,5):
        try:
            time.sleep(0.5)
            searchbox1 = driver.find_element(By.XPATH,"//div[contains(@class,'_aa61')]/div/div["+str(publ)+"]//div[contains(@class,'_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9p _abcm')]")
            searchbox1 = searchbox1.text
            searchbox2 = driver.find_element(By.XPATH,"//div[contains(@class,'_aa61')]/div/div["+str(publ)+"]//div[contains(@class,'_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9p  _abb- _abcm')]")
            searchbox2 = searchbox2.text
            arrayData.append({'username':searchbox1, 'name':searchbox2, 'url_profile': "https://www.instagram.com/"+searchbox1})
        except NoSuchElementException:  #Captura exepciones
            pass
    return(arrayData)