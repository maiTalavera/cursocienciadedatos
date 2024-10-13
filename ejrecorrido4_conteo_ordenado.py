#Para cada estación utilizada como inicio de un viaje, imprimirlas ordenadas por cantidad de viajes que iniciaron de la misma.
import requests
import pandas as pd
def wget(url):
    r = requests.get(url, allow_redirects=True)
    with open(url[url.rfind('/') + 1::], 'wb') as f:
        f.write(r.content)
wget ("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/recorridos-realizados-2021-sample.csv")
recorrido = pd.read_csv("recorridos-realizados-2021-sample.csv")
print(recorrido)
# Contar cuántos viajes iniciaron en cada estación
conteo_estaciones_inicio = recorrido['Id de estación de inicio'].value_counts()

# Ordenar las estaciones por cantidad de viajes (ya está en orden descendente por default)
estaciones_ordenadas = conteo_estaciones_inicio.sort_values(ascending=False)

# Imprimir las estaciones y sus conteos
print("Estaciones de inicio ordenadas por cantidad de viajes que iniciaron:")
for estacion, cantidad in estaciones_ordenadas.items():
    print(f"Estación {estacion}: {cantidad} viajes")