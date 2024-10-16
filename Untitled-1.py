#Averigüe cuál fue el número vendido de cada uno de los productos. 
#Determine cuáles clientes gastaron más de 50 pesos y ofrézcales un descuento la próxima vez que visiten el local. 
#Calcule cuánto gasta un cliente promedio en un dia en el local.
import requests
import pandas as pd
def wget(url):
     r = requests.get(url, allow_redirects=True)
     with open(url[url.rfind('/') + 1::], 'wb') as f:
        f.write(r.content)
wget ("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/datosClientes.xlsx")
datos = pd.read_excel("datosClientes.xlsx")
print(datos)
print("\nNombres de las columnas en el archivo:")
print(datos.columns)

nro_vendidos=datos= datos.groupby('Producto comprado')['Numero comprado'].sum()
print(nro_vendidos)
total_gastado = datos['Numero comprado'] * datos['Valor del producto']

# Mostrar el total gastado por cliente
print("\nTotal gastado por cada cliente:\n")
print(total_gastado)
