import pandas as pd
data = {
    'Producto': ['manzanas', 'naranjas', 'platanos', 'fresas'],
    'Cantidad': [50, 30, 20, 40],
    'Precio': [0.5, 0.6, 0.2, 1.0]
}
df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo CSV
df.to_csv('ventas.csv', index=False)

print("Archivo CSV creado con éxito.")

import pandas as pd

# Leer el archivo CSV
df_ventas = pd.read_csv('ventas.csv')

# Mostrar el contenido del DataFrame
print(df_ventas)
# Calcular el total de ventas
df_ventas['Total'] = df_ventas['Cantidad'] * df_ventas['Precio']

# Filtrar productos con total de ventas > 20
df_filtrado = df_ventas[df_ventas['Total'] > 20]

# Mostrar el DataFrame filtrado
print(df_filtrado)
# Agrupar por precio y calcular la suma de la cantidad
df_agrupado = df_ventas.groupby('Precio')['Cantidad'].sum().reset_index()

# Mostrar el DataFrame agrupado
print(df_agrupado)
