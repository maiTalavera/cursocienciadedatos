#¿Cuál es la duración promedio de cada viaje? (Los datos están en segundos
import requests
import pandas as pd
import numpy as np
def wget(url):
    r = requests.get(url, allow_redirects=True)
    with open(url[url.rfind('/') + 1::], 'wb') as f:
        f.write(r.content)
wget ("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/recorridos-realizados-2021-sample.csv")
recorrido = pd.read_csv("recorridos-realizados-2021-sample.csv")
print(recorrido)
# Filtrar duracion de viaje
columna_duracion = recorrido['Duración'] 
print(columna_duracion)
# Calcular el promedio
columna_duracion = pd.to_numeric(columna_duracion, errors='coerce')
total = columna_duracion.sum()
cantidad = columna_duracion.count()
promedio=total/cantidad
print(f"La duracion promedio de cada viaje es: {promedio}")
