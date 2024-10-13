#Importar el archivo Finanzas.xlsx que contiene la cantidad de dinero de los usuarios y las transferencias en dos hojas de archivo.
#Exportar un archivo usuarios_actualizados.xlsx que contiene las cantidades de dinero actualizadas.
import requests
import pandas as pd
def wget(url):
    r = requests.get(url, allow_redirects=True)
    with open(url[url.rfind('/') + 1::], 'wb') as f:
        f.write(r.content)
wget ("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/Finanzas.xlsx")
usuarios_df = pd.read_excel("Finanzas.xlsx", sheet_name="Usuarios", index_col="Usuario")
transferencias_df = pd.read_excel("Finanzas.xlsx", sheet_name="Transferencias")
# Mostrar los datos de usuarios y transferencias
print("Usuarios:")
print(usuarios_df)
print("\nTransferencias:")
print(transferencias_df)
print(usuarios_df.columns)

# Recorrer las transferencias y actualizar los saldos
for index, row in transferencias_df.iterrows():
    emisor = row['Emisor']
    receptor = row['Receptor']
    monto = row['Monto'] 
    # Actualizar el saldo del emisor (restar)
    usuarios_df.loc[emisor, 'Presupuesto'] -= monto
    # Actualizar el saldo del receptor (sumar)
    usuarios_df.loc[receptor, 'Presupuesto'] += monto
     #Mostrar los saldos actualizados
print("\nSaldos actualizados:")
print(usuarios_df)
# Exportar los saldos actualizados a un nuevo archivo Excel
usuarios_df.to_excel("usuarios_actualizados.xlsx")