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

    def pruebaNombreCapitulo(self):
        self.web = "https://www.animedatos.com/2019/02/capitulos-one-piece-sin-relleno.html"
        self.resultado= requests.get(self.web) # Obtenemos el contenido de la página
        self.contenido = self.resultado.text  # Lo pasamos a texto

        self.sooup = BeautifulSoup(self.contenido, 'lxml') # lxml es una libreria para parsear el html

        self.caja = self.sooup.find('div', id='post-toc') # Busca el elemento con la clase 'post-body entry-content'
        self.capitulo = self.caja.find('b').get_text()
        
        print(self.caja)

    
    
    

