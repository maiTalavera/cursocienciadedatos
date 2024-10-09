import pandas as pd
print(pd.__version__)  # Esto debería mostrar la versión de pandas instalada
import pandas as pd

# Crear un DataFrame simple
data = {
    'Nombre': ['Juan', 'Ana', 'Pedro', 'Laura'],
    'Edad': [28, 22, 35, 32],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']
}

df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo CSV
df.to_csv('datos_personales.csv', index=False)

print("Archivo CSV creado con éxito.")
