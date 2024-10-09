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
#¿Cual es la casa más cara? ¿Cuántas hay con este valor? Rta: 500001.0 - 814
archivo['median_house_value'] = pd.to_numeric(archivo['median_house_value'], errors='coerce')
# Obtener el valor máximo
casa_mas_cara=archivo['median_house_value'].max()
# Contar cuántas casas tienen ese valor máximo
cantidad_casas_mas_caras = archivo[archivo['median_house_value'] == casa_mas_cara].shape[0]
print(f"la casa mas cara es:{casa_mas_cara}")
print(f"Cantidad de casas con este valor: {cantidad_casas_mas_caras}")

      


