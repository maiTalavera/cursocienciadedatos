import requests

def wget(url):
    r = requests.get(url, allow_redirects=True)
    with open(url[url.rfind('/') + 1::], 'wb') as f:
        f.write(r.content)

wget ("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/Tabla1.xlsx")
import pandas as pd

df = pd.read_excel('Tabla1.xlsx')
Campeon = df.loc[df['Puntos'].idxmax(), 'Equipo']
Perdedor = df.loc[df['Puntos'].idxmin(), 'Equipo']
print(f"El grupo que salió en primer lugar es: {Campeon}")
print(f"El grupo que salió en último lugar es: {Perdedor}")

