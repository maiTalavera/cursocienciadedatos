#¿Cuántas estaciones diferentes fueron utilizadas?
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
# Combinar las estaciones de inicio y fin
estaciones_inicio_fin = pd.concat([recorrido['Id de estación de inicio'], recorrido['Id de estación de fin de viaje']])
# Contar las estaciones únicas en ambas columnas
estaciones= estaciones_inicio_fin.nunique()
print(f"El número total de estaciones diferentes utilizadas (inicio y fin) es: {estaciones}")


