import requests

# Descargar el archivo y leer los datos
def wget(url):
    r = requests.get(url, allow_redirects=True)
    with open(url[url.rfind('/') + 1::], 'wb') as f:
        f.write(r.content)

wget("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/Tabla1.xlsx")

import pandas as pd
df = pd.read_excel('Tabla1.xlsx')

# Calcular la diferencia de goles
df['Diferencia de goles'] = df['Goles a favor'] - df['Goles en contra']

# Filtrar los equipos que tienen más de 20 puntos y mostrar las columnas "Equipo", "Puntos" y "Diferencia de goles"
mayores = df.loc[df['Puntos'] > 20, ['Equipo', 'Puntos', 'Diferencia de goles']]
print(f"Los equipos que obtuvieron más de 20 puntos: \n{mayores}")

# Ordenar los equipos por puntaje en orden descendente
Mayores_ordenado = mayores.sort_values(by='Puntos', ascending=False)
print("\nEquipos ordenados por puntos de mayor a menor:")
print(Mayores_ordenado)

# Encontrar el equipo con mayor y menor puntaje
Mayor_Puntaje = df.loc[df['Puntos'].idxmax(), 'Equipo']
Menor_Puntaje = df.loc[df['Puntos'].idxmin(), 'Equipo']

# Imprimir los resultados
print(f"\nEl grupo que salió en primer lugar es: {Mayor_Puntaje}")
print(f"El grupo que salió en último lugar es: {Menor_Puntaje}")


