import time
import ssl
import os
import json
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

load_dotenv()

def getAnalisisPostTwitter(self,nombres):
    # Variables de entorno
    print("NOMBRE:",nombres)
    USER = "985504635"
    PASSWORD = "Marcelo1609"

    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)

    driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe', chrome_options=chrome_options)
    driver.get("https://twitter.com/i/flow/login")
    driver.maximize_window()

    ssl._create_default_https_context = ssl._create_unverified_context

    # login
    try:
        time.sleep(3)
        username = driver.find_element("css selector", "input[name='text']")
        username.clear()
        username.send_keys(USER)
        nextStep1= driver.find_element('css selector','#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > div > div > div:nth-child(6) > div > span').click()
        time.sleep(3)
        password = driver.find_element("css selector", "input[name='password']")
        password.clear()
        password.send_keys(PASSWORD)
        time.sleep(3)
        print(">>>>>>>>>: Ingreso 1",)
        nextStep2= driver.find_element('css selector',"#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-1isdzm1 > div > div.css-1dbjc4n > div > div > div").click()
        time.sleep(3)
        optionSearch = driver.find_element('css selector', '#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-aqfbo4.r-zso239.r-1hycxz > div > div.css-1dbjc4n.r-gtdqiz.r-1hycxz > div > div > div > div.css-1dbjc4n.r-1awozwy.r-aqfbo4.r-14lw9ot.r-18u37iz.r-1h3ijdo.r-6gpygo.r-15ysp7h.r-1xcajam.r-ipm5af.r-1hycxz.r-136ojw6 > div > div > div > form > div.css-1dbjc4n.r-1wbh5a2 > div > div > div > label > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2 > div > input')
        optionSearch.clear()
        print(">>>>>>>>>: Ingreso 2",)
        time.sleep(3)
        optionSearch.send_keys(nombres)
        time.sleep(10)
        print(">>>>>>>>>: Ingreso 3",)
        optionSearch = driver.find_element('css selector', '#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-aqfbo4.r-zso239.r-1hycxz > div > div.css-1dbjc4n.r-gtdqiz.r-1hycxz > div > div > div > div.css-1dbjc4n.r-1awozwy.r-aqfbo4.r-14lw9ot.r-18u37iz.r-1h3ijdo.r-6gpygo.r-15ysp7h.r-1xcajam.r-ipm5af.r-1hycxz.r-136ojw6 > div > div > div > form > div.css-1dbjc4n.r-1wbh5a2 > div > div > div > label > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2 > div > input').send_keys(Keys.ENTER)
        time.sleep(3)
        print(">>>>>>>>>: Ingreso 4",)
        optionSearch = driver.find_element('css selector', '#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-14lw9ot.r-jxzhtn.r-1ljd8xs.r-13l2t4g.r-1phboty.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c > div > div.css-1dbjc4n.r-aqfbo4.r-gtdqiz.r-1gn8etr.r-1g40b8q > div.css-1dbjc4n.r-1e5uvyk.r-6026j > div.css-1dbjc4n.r-136ojw6 > div > div > div > div > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1pi2tsx.r-1777fci > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-16y2uox.r-1wbh5a2.r-4amgru.r-itp27i > div > div > div > form > div.css-1dbjc4n.r-1wbh5a2 > div > div > div > label > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2 > div > input').click()
        time.sleep(3)
        print(">>>>>>>>>: Ingreso 5",)
        selectPerfil = driver.find_element('css selector', '#typeaheadDropdown-2 > div:nth-child(3) > div > div').click()
        time.sleep(3)
        print(">>>>>>>>>: Ingreso 6",)
        selectTwets = driver.find_element('css selector', '#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-14lw9ot.r-jxzhtn.r-1ljd8xs.r-13l2t4g.r-1phboty.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c')
        time.sleep(3)
        print(">>>>>>>>>: Ingreso 7",)
        url = driver.current_url
        driver.get(url)
        print(">>>>>>>>>: Ingreso 8",)
        time.sleep(3)
            
        for j in range(0):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(5)
        anchors = driver.find_elements("tag name", "a")
        time.sleep(3)
        anchors = [a.get_attribute('href') for a in anchors]
        time.sleep(3)
        print(">>>>>>>>>: url",url)
        anchors = [a for a in anchors if str(a).startswith(url +"/status")]
        time.sleep(3)

    except NoSuchElementException:  #No encontro a la persona
        print(">>>>>>>>>: Catch Usuario")
        anchors =[]
        pass

    keyWords = ['puta','putísima','Carajo','MIERDA','UPC','cryproot','Device','Developer','Amor','amor','Matar', 'Asesinar', 'Amenazar','Golpear','Pistola','Arma','Arma de fuego','Amor','Violar','Abusar Sexualmente','Marihuana','Amenaza','bandido','HP','asaltar']
    arrayData = []

    for post in anchors:
        driver.get(post)
        time.sleep(2)

        #obtener Comentario
        try:
            comentario= driver.find_element(By.XPATH,"//div[contains(@class,'css-901oao r-18jsvk2 r-37j5jr r-1blvdjr r-16dba41 r-vrz42v r-bcqeeo r-bnwqim r-qvutc0')]") if driver.find_element(By.XPATH,"//div[contains(@class,'css-901oao r-18jsvk2 r-37j5jr r-1blvdjr r-16dba41 r-vrz42v r-bcqeeo r-bnwqim r-qvutc0')]") else ''
            comentario = comentario.text
            print(">>>>>>>>>: Ingreso analisis de comentarios",url)
        except NoSuchElementException:  #captura errores
            print(">>>>>>>>>: Catch Comentario")
            pass

        #obtener foto
        try:
            images = driver.find_elements("tag name", "img")
            images = [image.get_attribute('src') for image in images]
            foto = ""
            for item in images:    
                if 'https://pbs.twimg.com/media/' in item:
                    foto = item
        except NoSuchElementException:  #captura errores
            pass

        palabraEcontrada = ''
        for item in keyWords:    
            if item in comentario:
                palabraEcontrada = item
        
        arrayData.append({'Publicacion': comentario, 'image':foto,'palabraEcontrada':palabraEcontrada })
    return(arrayData)
    # res = json.dumps(arrayData)


