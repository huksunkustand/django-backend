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

def getAnalisisInstagramPublicacionesSelenium(self,profile):
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
    nothow = driver.find_element("xpath", "//button[contains(text(), 'Ahora no')]").click()
    # turn on notif
    time.sleep(4)
    nothow2 = driver.find_element("xpath", "//button[contains(text(), 'Ahora no')]").click()

    # searchbox
    time.sleep(7)
    searchbox = driver.find_element("css selector", "input[placeholder='Buscar']")
    searchbox.clear()
    searchbox.send_keys(profile) #jtandazo
    time.sleep(3)
    searchbox.send_keys(Keys.ENTER)
    time.sleep(3)
    searchbox.send_keys(Keys.ENTER)
    time.sleep(3)
    # Scroll
    scrolldown = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
    match = False
    while (match == False):
        last_count = scrolldown
        time.sleep(3)
        scrolldown = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
        if last_count == scrolldown:
            match = True
    time.sleep(2)
    posts = []
    links = driver.find_elements("tag name", "a")
    for link in links:
        post = link.get_attribute('href')
        if '/p/' in post:
            posts.append(post)

    keyWords = ['puta','putísima','Carajo','MIERDA','UPC','cryproot','Device','Developer','Amor','amor','Matar', 'Asesinar', 'Amenazar','Golpear','Pistola','Arma','Arma de fuego','Amor','Violar','Abusar Sexualmente']
    arrayData = []

    if(len(posts) <= 15):
        try:
            for soyu in posts:
                driver.get(soyu)
                time.sleep(2)
                texto=driver.find_element(By.XPATH,"//div[contains(@class,'_aa6b _ad9f _aa6d')]")
                texto=texto.text
                palabraEcontrada = ''
                for item in keyWords:    
                    if item in texto:
                        palabraEcontrada = item
                arrayData.append({'Urlphoto': posts, 'Publicacion': texto,'palabraEcontrada':palabraEcontrada})
                #arrayData.append(texto)
        except NoSuchElementException:  #Captura exepciones
            pass

        else:
            soloimprime15 = posts[:15]
            for soyu in soloimprime15:
                driver.get(soyu)
                time.sleep(2)
                texto=driver.find_element(By.XPATH,"//div[contains(@class,'_aa6b _ad9f _aa6d')]")
                texto=texto.text
                palabraEcontrada = ''
                for item in keyWords:    
                    if item in texto:
                        palabraEcontrada = item
                arrayData.append({'Urlphoto': posts, 'Publicacion': texto,'palabraEcontrada':palabraEcontrada})
    return(arrayData)