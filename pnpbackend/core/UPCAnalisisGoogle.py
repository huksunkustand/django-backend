import time
import ssl
from dotenv import load_dotenv
import os
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

load_dotenv()

def getAnalisisGoogle(self,name):

    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)

        #####background
    chromeOptions = Options()
    chromeOptions.headless = True
    ##########
    
    # driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe', chrome_options=chrome_options)
    driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe', options=chromeOptions)

    driver.get("https://www.google.com/search?q="+name)

    ssl._create_default_https_context = ssl._create_unverified_context
    time.sleep(4)

    keyWords = ['puta','putísima','Carajo','MIERDA','UPC','cryproot','Device','Developer','Amor','amor','Matar', 'Asesinar', 'Amenazar','Golpear','Pistola','Arma','Arma de fuego','Amor','Violar','Abusar Sexualmente']
    arrayData  = []

    for publ in range(1,8):
        url = ''
        palabraencontrada = ''
        descripcion = ''
        try:
            searchbox2 = driver.find_element(By.XPATH,"//div[contains(@class,'v7W49e')]/div["+str(publ)+"]")
            descripcion = searchbox2.text
            
            for item in keyWords:    
                if item in descripcion:
                    palabraencontrada = item
        except NoSuchElementException:  #captura errores
            pass
            
        try:
            if "Imágenes" not in descripcion:
                url = driver.find_element(By.XPATH,"//div[contains(@class,'v7W49e')]/div["+str(publ)+"]//div[contains(@class,'Z26q7c UK95Uc jGGQ5e')]/div/a").get_attribute('href')
        except NoSuchElementException:  #captura errores
            pass
            
        time.sleep(1.5)
        arrayData.append({'URL': url, 'Descripcion':descripcion,'PalabraEncontrada':palabraencontrada })

    return(arrayData)
