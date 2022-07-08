from bs4 import BeautifulSoup
import requests


class ObtenerUltimoCapitulo:

    website = "https://www3.animeflv.to/anime/one-piece-tv"
    result= requests.get(website) # Obtenemos el contenido de la página
    content = result.text  # Lo pasamos a texto

    soup = BeautifulSoup(content, 'lxml') # lxml es una libreria para parsear el html

    #print(soup)

    # Orden de busqueda de elementos
    # ID
    # Class name
    # Tag name, CSS Selector
    # Xpath
    
    def get_last_episode(self):
        box = self.soup.find('li', class_='fa-play-circle') # Busca el elemento con la clase 'fa-play-circle'
        cap = box.find('p').get_text().split() # Obtiene el texto del elemento y lo separa por el espacio
        ultimocap = cap[1]
        #print(ultimocap) # Imprime el segundo elemento del array
        return ultimocap
    
    

