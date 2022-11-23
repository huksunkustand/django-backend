import time
import ssl
from dotenv import load_dotenv
import os
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

load_dotenv()

def getAnalisisFotos(self,profile):
    # Variables de entorno
    print("profile:",profile)
    FACEBOOK_USER = os.getenv("FACEBOOK_USER")
    FACEBOOK_PASSWORD = os.getenv("FACEBOOK_PASSWORD")

    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)

     #####background
    chromeOptions = Options()
    chromeOptions.headless = True
    ##########
    print(">>>>>>>>>>>>>>>> Entro Bloque 2:<<<<<<<<<<<<<<<<<<<<<",)
    # driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe', chrome_options=chrome_options)
    driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe', options=chromeOptions)
    driver.get("https://www.facebook.com/login/")

    ssl._create_default_https_context = ssl._create_unverified_context

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
    print(">>>>>>>>>>>>>>>> Entro Bloque 3:<<<<<<<<<<<<<<<<<<<<<",)
    for i in ["photos_of", "photos_by"]:
        
        driver.get("https://www.facebook.com/"+ profile +"/" + i + "/")
        time.sleep(3)
        
        
        for j in range(0,1):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)

        anchors = driver.find_elements("tag name", "a")
        anchors = [a.get_attribute('href') for a in anchors]
        anchors = [a for a in anchors if str(a).startswith("https://www.facebook.com/photo")]
    
    keyWords = ['puta','putísima','Carajo','MIERDA','UPC','cryproot','Device','Developer','Amor','amor','Matar', 'Asesinar', 'Amenazar','Golpear','Pistola','Arma','Arma de fuego','Amor','Violar','Abusar Sexualmente']
    arrayData = []

    # print("anchors:",anchors)
    if(len(anchors) <= 20):
        for post in anchors:
            driver.get(post)
            time.sleep(2)
            # texto= driver.find_element(By.XPATH,"//div[contains(@class,'xkhd6sd x1g2khh7 x4uap5 xyinxu5')]") if driver.find_element(By.XPATH,"//div[contains(@class,'xkhd6sd x1g2khh7 x4uap5 xyinxu5')]") != '' else ''
            texto= driver.find_element(By.XPATH,"//div") if driver.find_element(By.XPATH,"//div") != '' else ''
            texto=texto.text

            images = driver.find_elements("tag name", "img")
            images = [image.get_attribute('src') for image in images]

            # pub_numero=2
            # fecha=driver.find_element(By.XPATH,"//div[contains(@class,'x78zum5 xdt5ytf xz62fqu x16ldp7u')]/div["+str(pub_numero)+"]")
            fecha=driver.find_element(By.XPATH,"//div[contains(@class,'xyamay9 x1pi30zi xsag5q8 x1swvt13')]/div/div")
            fecha=fecha.text  
            palabraEcontrada = ''
            for item in keyWords:    
                if item in texto:
                    palabraEcontrada = item
            arrayData.append({'Urlphoto': post, 'Publicacion': texto, 'Fecha': fecha, 'image':images[0],'palabraEcontrada':palabraEcontrada})
        return(arrayData)
    else:
        soloimprime20 = anchors[:20]
        for post in soloimprime20:
            driver.get(post)
            time.sleep(2)
            #texto= driver.find_element(By.XPATH,"//div[contains(@class,'xkhd6sd x1g2khh7 x4uap5 xyinxu5')]") if driver.find_element(By.XPATH,"//div[contains(@class,'xkhd6sd x1g2khh7 x4uap5 xyinxu5')]") != '' else ''
            texto= driver.find_element(By.XPATH,"//div") if driver.find_element(By.XPATH,"//div") != '' else ''
            texto=texto.text

            images = driver.find_elements("tag name", "img")
            images = [image.get_attribute('src') for image in images]

            #pub_numero=2
            #fecha=driver.find_element(By.XPATH,"//div[contains(@class,'x78zum5 xdt5ytf xz62fqu x16ldp7u')]/div["+str(pub_numero)+"]")
            fecha=driver.find_element(By.XPATH,"//div[contains(@class,'xyamay9 x1pi30zi xsag5q8 x1swvt13')]/div/div")
            fecha=fecha.text  
            palabraEcontrada = ''
            for item in keyWords:    
                if item in texto:
                    palabraEcontrada = item
            arrayData.append({'Urlphoto': post, 'Publicacion': texto, 'Fecha': fecha, 'image':images[0],'palabraEcontrada':palabraEcontrada})
    return(arrayData)
