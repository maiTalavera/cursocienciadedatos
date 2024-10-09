#¿Qué porcentaje de los viajes se completaron en estado NORMAL?
import requests
import pandas as pd
import numpy as np
def wget(url):
    r = requests.get(url, allow_redirects=True)
    with open(url[url.rfind('/') + 1::], 'wb') as f:
        f.write(r.content)
wget ("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/recorridos-realizados-2021-sample.csv")
recorrido = pd.read_csv("recorridos-realizados-2021-sample.csv")
print(recorrido.columns)
 # Esto te mostrará cuántas columnas tiene el DataFrame
print(recorrido.head())
viajes_normales = recorrido[recorrido['Estado cerrado'] == 'NORMAL']
# Calcular el porcentaje
total_viajes = len(recorrido)
viajes_completados = len(viajes_normales)
porcentaje = (viajes_completados / total_viajes) * 100
print(f"El porcentaje de viajes completados en estado NORMAL es: {porcentaje:.2f}%")

