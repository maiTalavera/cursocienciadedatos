import pandas as pd
data = {
    'Producto': ['manzanas', 'nanaranjas', 'platanos', 'fresas'],
    'Cantidad': [50, 30, 20, 40],
    'Precio': [0.5, 0.6, 0.2, 1.0]
}
df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo CSV
df.to_csv('ventas.csv', index=False)

print("Archivo CSV creado con éxito.")