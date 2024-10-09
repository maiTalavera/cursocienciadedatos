import pandas as pd

datos = pd.read_excel("Datos.xlsx")
print(datos)
# Filtrar notas de quimica
columna_qx = datos['Quimica'] 
print(columna_qx)
# Calcular el promedio
columna_qx = pd.to_numeric(columna_qx, errors='coerce')
total = columna_qx.sum()
cantidad = columna_qx.count()
promedio=total/cantidad
print(f"El promedio de las notas de Química es: {promedio}")

