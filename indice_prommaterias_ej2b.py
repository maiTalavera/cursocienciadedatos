import pandas as pd
datos = pd.read_excel("Datos.xlsx")
print(datos)
#indice
indice = 0
alumno = datos.loc[indice]
print(alumno)
# Calcular el promedio de materias
promedios = (alumno['Quimica'] + alumno['Matematica'] + alumno['Fisica']) / 3
print(promedios)

