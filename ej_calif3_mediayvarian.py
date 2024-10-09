# Obtener la media y la varianza de la propiedad 'median_house_value'. Rta: 207300.91 - 13451442293.57
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
archivo['median_house_value'] = pd.to_numeric(archivo['median_house_value'], errors='coerce')
# Media
media = archivo['median_house_value'].mean()
# Varianza
varianza = archivo['median_house_value'].var()

print(f"Media: {media}")
print(f"Varianza: {varianza}")