#¿A qué hora del día se realizaron más viajes? (por ejemplo: de 16hs a 17hs)
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
recorrido['Fecha de inicio'] = pd.to_datetime(recorrido['Fecha de inicio'], errors='coerce')
recorrido['Hora'] = recorrido['Fecha de inicio'].dt.hour
conteo_viajes_por_hora = recorrido['Hora'].value_counts().sort_index()
hora_mas_viajes = conteo_viajes_por_hora.idxmax()
cantidad_viajes = conteo_viajes_por_hora.max()
print(f"La hora con más viajes es: {hora_mas_viajes}:00, con un total de {cantidad_viajes} viajes.")


