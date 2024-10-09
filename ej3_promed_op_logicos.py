#Obtener el promedio general sólo para aquellos alumnos que aprobaron Matemática (con nota >= 6) en el archivo Datos.xlsx.
import requests
def wget(url):
    r = requests.get(url, allow_redirects=True)
    with open(url[url.rfind('/') + 1::], 'wb') as f:
        f.write(r.content)
wget ("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/Datos2.xlsx")
import pandas as pd
datos2 = pd.read_excel("Datos2.xlsx")
print("Datos:\n")
print(datos2)
datos2['Matematica'] = pd.to_numeric(datos2['Matematica'], errors='coerce')
aprobados = datos2[ datos2['Matematica'] >= 6 ]
print("\nAprobados en Matematica:\n")
print(aprobados)
total = datos2['Matematica'].sum()
cantidad = datos2['Matematica'].count()
promedio=total/cantidad
print(f"El promedio de las notas de Química es: {promedio}")



