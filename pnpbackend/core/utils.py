import requests, json

def FiltrarNombre(nombre,listArray):
    arrayFiltrado = []
    for item in listArray:
      if nombre.lower() in str(item['name'].lower()):
         arrayFiltrado.append(item)
    return(arrayFiltrado)

def DiccionarioPalabrasDelictivas ():
    keyWords = [
           'puta','putísima','Carajo','MIERDA','UPC','cryproot','Device','Developer','Amor',
           'amor','Matar', 'Asesinar', 'Amenazar','Golpear','Pistola','Arma','Arma de fuego','Amor',
           'Violar','Abusar Sexualmente','Marihuana','Amenaza','bandido','HP','asaltar']
    return keyWords

def getInfoInstagram(myname):
    permanent_cookie = "sessionid={}".format(myname)
    myheaders = {
        "X-IG-App-ID": "936619743392459",
        "Cookie": permanent_cookie,
    }
    #Consulta el Info profile instagram
    sample_url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={myname}"
    sample = requests.get(sample_url, headers=myheaders)
    data = json.loads(sample.text)
    return(data)