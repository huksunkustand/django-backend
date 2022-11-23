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

load_dotenv()

def getAnalisisPerfilSelenium(self,nombres):
        # Variables de entorno
    FACEBOOK_USER = "985504635"
    FACEBOOK_PASSWORD = "Marcelo1609"

    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)

    #####background
    chromeOptions = Options()
    chromeOptions.headless = True
    ##########
    
    # driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe', chrome_options=chrome_options)
    driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe', options=chromeOptions)
    
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
    password.send_keys(FACEBOOK_PASSWORD)
    login = driver.find_element("css selector", "button[type='submit']").click()
    time.sleep(6)
    name = nombres
    driver.get("https://www.facebook.com/search/people/?q="+name)
    time.sleep(5)
    #Imagenes de los primero 4 perfiles
    torres = driver.find_elements("tag name", "image")
    #torres = driver.find_elements("tag name", "image[style='height: 60px; width: 60px;']")
    torres = [image.get_attribute('xlink:href') for image in torres]
    arrayData1 = [torres[1],torres[2],torres[3],torres[4]]
    #aqui termina las imagenes
    arrayData  = []
    arrayData3 = []

    for publ in range(1,5):
        # searchbox1 = driver.find_element(By.XPATH,"//div[contains(@class,'x193iq5w x1xwk8fm')]/div["+str(publ)+"]//div[contains(@class,'xq8finb xl56j7k x78zum5 x1cy8zhl')]/div/a").get_attribute('href')
        searchbox1 = driver.find_element(By.XPATH,"//div[contains(@class,'x193iq5w x1xwk8fm')]/div["+str(publ)+"]//div[contains(@class,'xw7yly9 xktsk01 x1yztbdb x1d52u69')]/div/div/div/div/a").get_attribute('href')
        arrayData.append(searchbox1)
        #nombre
        searchbox2 = driver.find_element(By.XPATH,"//div[contains(@class,'x193iq5w x1xwk8fm')]/div["+str(publ)+"]//div[contains(@class,'xu06os2 x1ok221b')]")
        searchbox2=searchbox2.text
        arrayData3.append('')

        time.sleep(1.5)

    arrayData2 = []
    for soyu in arrayData:
        if "&__tn__=%3C" and 'profile' in soyu:
            t = urlparse(soyu)
            d = parse_qs(t.query)
            value = d.get("id")
            arrayData2.append(value[0])
            continue
        if "?__tn__" in soyu:
            stringdata = soyu
            data_split = stringdata.split("/")
            data=data_split[3]
            stringdata1 = data
            data_split1 = stringdata1.split("?")
            data1=data_split1[0]
            arrayData2.append(data1)
            continue
        if "profile" in soyu:
            data = (soyu.split('=')[1])
            arrayData2.append(data)
        else:
            stringdata = soyu
            data_split = stringdata.split("/")
            data=data_split[3]
            arrayData2.append(data[3])

    # result = [{"url_profile": a, "profile_picture": b, "username": c , d: "nombres" } for a, b, c,d in zip(arrayData, arrayData1, arrayData2, arrayData3)]
    result = [{"url_profile": a, "profile_picture": b, "username": c, "name": d } for a, b, c, d in zip(arrayData, arrayData1, arrayData2, arrayData3)]
    return(result)