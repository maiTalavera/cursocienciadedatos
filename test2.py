#Importar el archivo Finanzas.xlsx que contiene la cantidad de dinero de los usuarios y las transferencias en dos hojas de archivo.
#Exportar un archivo usuarios_actualizados.xlsx que contiene las cantidades de dinero actualizadas.
import requests
import requests
import pandas as pd
def wget(url):
    r = requests.get(url, allow_redirects=True)
    with open(url[url.rfind('/') + 1::], 'wb') as f:
        f.write(r.content)
wget ("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/Finanzas.xlsx")
usuarios_archivo = pd.read_excel("Finanzas.xlsx", "Usuarios")
#leemos los usuarios "indexados" por su nombre

transferencias_archivo = pd.read_excel("Finanzas.xlsx", "Transferencias")
print(transferencias_archivo)
print(usuarios_archivo)
emisores = transferencias_archivo['Emisor']
receptores= transferencias_archivo['Receptor']
montos = transferencias_archivo['Monto']
usuarios = usuarios_archivo['Usuario']
for emisor in range(len(transferencias_archivo['Emisor'])):
  print(f"emisor: {emisores[emisor]} : {montos[emisor]}")
  for idxUsr in range(len(usuarios_archivo['Usuario'])):
    if emisores[emisor] == idxUsr:
      print("emisor: {emisor}")
      print("\nSaldos actualizados:")
print(emisor)

     #Mostrar los saldos actualizados
emisor.to_excel("usuarios_actualizados.xlsx")
