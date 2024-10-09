#Armar una función que copie un archivo .xlsx, y lo guarde como "Copia 1 -  nombre ", de ya existir debe guardarlo como Copia 2 -, Copia 3 - , ...
#Usar la libreria os para chequear si existe el archivo. Tips:
#os.path.exists( nombre ) devolverá True si ya existe
#Se puede importar con: import os
import os
import shutil
def copiar_archivo (inventario): 
    # Obtener el nombre base sin extensión y la extensión
    nombre_base, extension = os.path.splitext(inventario)
    if extension != '.xlsx':
        print("El archivo debe ser un archivo .xlsx")
        return
    # Inicializamos contador
    contador = 1
    nuevo_nombre = f"Copia {contador} - {nombre_base}{extension}"
    # Chequeamos si el archivo ya existe
    while os.path.exists(nuevo_nombre):
        contador += 1
        nuevo_nombre = f"Copia {contador} - {nombre_base}{extension}"
        # Copiamos el archivo con el nuevo nombre
    shutil.copy2(inventario, nuevo_nombre)
    print(f"Archivo copiado como: {nuevo_nombre}")

copiar_archivo("inventario.xlsx")