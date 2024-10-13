#Averigüe cuál fue el número vendido de cada uno de los productos. 
#Determine cuáles clientes gastaron más de 50 pesos y ofrézcales un descuento la próxima vez que visiten el local. 
#Calcule cuánto gasta un cliente promedio en un dia en el local.
import requests
import pandas as pd
import numpy as np  
def wget(url):
     r = requests.get(url, allow_redirects=True)
     with open(url[url.rfind('/') + 1::], 'wb') as f:
        f.write(r.content)
wget ("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/datosClientes.xlsx")
datos = pd.read_excel("datosClientes.xlsx")
print(datos)
print("\nNombres de las columnas en el archivo:")
print(datos.columns)
nro_vendidos = datos.groupby('Producto comprado')['Numero comprado'].sum()
print(nro_vendidos)
# Calcular y mostrar el total vendido de cada producto
for i in range(len(datos['Producto comprado'])):
    total_vendido = datos['Numero comprado'][i] * datos['Valor del producto'][i]
    print(f"Producto: {datos['Producto comprado'][i]}, Total vendido: {total_vendido}")
    if total_vendido >50:
     print('La proxima compra tendrá descuento')
     gasto_promedio = np.mean(total_vendido)  
     print('gasto promedio del cliente en un dia', gasto_promedio)