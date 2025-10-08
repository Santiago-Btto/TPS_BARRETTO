# -*- coding: utf-8 -*-

# Nombre del archivo que queremos leer (ruta relativa)
RUTA_ARCHIVO = "C:\Users\Santiago\Desktop\faku\Programacion I\Git_PRO1\HUALPA\CLASE 8_10"

try:
    # Abrimos el archivo en modo lectura
    archivo = open(RUTA_ARCHIVO, "r", encoding="utf-8")
    #archivo = open(RUTA_ARCHIVO, "r")
    
    print("Contenido del archivo:\n")

    # Recorremos línea por línea
    for linea in archivo:
        nombre = linea.strip()  # Quitamos espacios y saltos de línea
        print(nombre)

except FileNotFoundError:
    print(f"Error: no se encontró el archivo '{RUTA_ARCHIVO}'. Verificá la ruta o el nombre.")
except PermissionError:
    print(f"Error: no tenés permisos para leer el archivo '{RUTA_ARCHIVO}'.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
finally:
    # Cerramos el archivo si fue abierto correctamente
    try:
        archivo.close()
    except NameError:
        # Si el archivo nunca se abrió, evitamos error en close()
        pass
