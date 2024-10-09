import requests

def wget(url):
    r = requests.get(url, allow_redirects=True)
    with open(url[url.rfind('/') + 1::], 'wb') as f:
        f.write(r.content)

wget ("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/Tabla1.xlsx")
import pandas as pd

archivo = pd.read_excel("Tabla1.xlsx")
print(archivo)
import pandas as pd
archivo = pd.read_excel("Tabla1.xlsx", index_col ="Equipo")
print(archivo)

data = archivo.to_dict("index")
print(data)
print(data['Equipo A'])          
print(f"Equipo A: {data['Equipo A']['Goles a favor'] - data['Equipo A']['Goles en contra']}")
