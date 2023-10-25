import urllib.request

url = "https://pldb.com/columns.csv" # Enlace del archivo a descargar
ubicacion = "C:/Users/Public/Desktop/columns.csv" # Ubicación donde se guardará el archivo descargado

# Descargar el archivo y guardarlo en la ubicación especificada
urllib.request.urlretrieve(url, ubicacion)

print("El archivo ha sido descargado en", ubicacion)
print("")
input("Presione Enter para salir...")