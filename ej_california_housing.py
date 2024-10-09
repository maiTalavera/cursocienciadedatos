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
#¿Cuantas casas hay con valor 'median_house_value' mayor a 80000 tomando de la longitud -120 a -118? Rta: 5466
archivo['median_house_value'] = pd.to_numeric(archivo['median_house_value'], errors='coerce')
casas_median = archivo[(archivo['median_house_value'] > 80000 )  & (archivo['longitude'] >= -120) & (archivo['longitude'] <= -118)]
print("\nCasas median house mayor a 80000:\n")
print(casas_median)
# Contar cuántas casas cumplen la condición
cantidad_casas = casas_median.shape[0]
print(f"\nCantidad de casas que cumplen la condición: {cantidad_casas}")
#¿Cual es el promedio de habitaciones por manzana ('total_rooms') de estas casas? Rta: 2466.31
archivo['total_rooms'] = pd.to_numeric(archivo['total_rooms'], errors='coerce')
habitaciones = archivo[ archivo['total_rooms'] ]
print("\nhabitaciones por manzana ('total_rooms'):\n")
print(habitaciones)
total = archivo['total_rooms'].sum()
cantidad = archivo['total_rooms'].count()
promedio=total/cantidad
print(f"El promedio es: {promedio}")
#¿Cual es la casa más cara? ¿Cuántas hay con este valor? Rta: 500001.0 - 814
archivo['median_house_value'] = pd.to_numeric(archivo['median_house_value'], errors='coerce')
casa_mas_cara=archivo.max()
cantidad = archivo.count()>= casa_mas_cara
print(f"la casa mas cara es:{casa_mas_cara}")
print(f"hay con este valor: {cantidad}")

      

