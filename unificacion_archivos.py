#
import requests
import pandas as pd
def wget(url):
    r = requests.get(url, allow_redirects=True)
    with open(url[url.rfind('/') + 1::], 'wb') as f:
        f.write(r.content)
wget ("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/lista1.csv")
wget ("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/lista2.csv")
lista1 = pd.read_csv("lista1.csv")
lista2 = pd.read_csv("lista2.csv")
listafinal = pd.concat([lista1, lista2], ignore_index=True)
listafinal.to_csv("listafinal.csv", index=False)
print("Las listas han sido combinadas y guardadas en listafinal.csv.")
