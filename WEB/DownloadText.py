import requests
from bs4 import BeautifulSoup

# URL de la página web que deseas descargar
url = 'https://hadoop.apache.org/'

# Realizamos la solicitud HTTP
response = requests.get(url)

if response.status_code == 200:
    # Parseamos el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontramos todo el texto en la página web
    page_text = soup.get_text()

    # Guardamos el texto en un archivo .txt
    with open('contenido_web.txt', 'w', encoding='utf-8') as txt_file:
        txt_file.write(page_text)
    print("Texto guardado exitosamente en 'contenido_web.txt'")
else:
    print(f"Error al obtener la página. Código de estado: {response.status_code}")
