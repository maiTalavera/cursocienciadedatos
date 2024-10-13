import requests
import pandas as pd
import numpy as np

def wget(url):
    r = requests.get(url, allow_redirects=True)
    with open(url[url.rfind('/') + 1::], 'wb') as f:
        f.write(r.content)
wget ("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/california_housing_train.xlsx")
archivo = pd.read_excel("california_housing_train.xlsx")
print(archivo.head())
paso = .5

lats = np.arange(32.5,42.5,paso)
lons = np.arange(-124.3,113.3,paso)
maximoValor = 0
maximaLat = 0
maximaLon = 0