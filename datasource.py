import urllib.request

url = "https://pldb.pub/pldb.csv" # Enlace del archivo a descargar

# Descargar el archivo y guardarlo en la ubicación especificada
urllib.request.urlretrieve(url, "datasource.csv")

print("El archivo datasource.csv ha sido descargado")
print("")
input("Presione Enter para salir...")