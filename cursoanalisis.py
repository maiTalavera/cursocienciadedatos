import requests

def wget(url):
    r = requests.get(url, allow_redirects=True)
    with open(url[url.rfind('/') + 1::], 'wb') as f:
        f.write(r.content)

wget("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/Datos.xlsx")
import pandas as pd

archivo = pd.read_excel("Datos.xlsx")
# La variable archivo es de un tipo de dato especial de pandas llamado 'DataFrame'
print(archivo)
import pandas as pd
archivo = pd.read_excel("Datos.xlsx", index_col ="Apellido")
print(archivo)
archivo = pd.read_excel("Datos.xlsx", index_col ="Apellido")
print(archivo)
data = archivo.to_dict("index")
print(data)
print(data['Lagos'])           
print(data['Lagos']['Legajo'])