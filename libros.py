import requests
from bs4 import BeautifulSoup

import os



def libros_sitio_web(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanzar una excepción si ocurre un error HTTP
        html = response.text
    except requests.exceptions.RequestException as e:
        print("Error en la solicitud:", e)
        return

    soup = BeautifulSoup(html, 'html.parser')

    directorio_destino = 'libro_descargado'
    try:
        if not os.path.exists(directorio_destino):
            os.makedirs(directorio_destino)
    except OSError as e:
        print("Error al crear el directorio:", e)
        return



    print("Libro descargado!")

# URL del sitio web del libro
url_sitio_web = input("Introduce la URL del sitio web: ")
libros_sitio_web(url_sitio_web)

# Abre el archivo index.html en un navegador para visualizarlo localmente
import webbrowser
ruta_index_html = os.path.join('libro_descargado', 'index.html')
webbrowser.open(ruta_index_html)



#Arreglo que arroja la cadena de la pagina
arreglo = []
cadenas = ["LPM", "MLA", "PAA", "PCA", "PEA", "SDA", "TPA"]

for i in range(1, 7):
    for cadena in cadenas:
        elemento = f'P{i}{cadena}'
        enlace = f'https://www.conaliteg.sep.gob.mx/2023/c/{elemento}.htm'
        arreglo.append(enlace)

for enlace in arreglo:
    print(enlace)
