import pandas as pd

# Lee el archivo CSV en un DataFrame de pandas
datos = pd.read_csv('datasource.csv', low_memory=False)

# Selecciona solo las columnas necesarias
datos_nuevos = datos[['title', 'type', 'bookCount', 'paperCount', 'numberOfUsersEstimate', 'numberOfJobsEstimate', 'githubLanguage_repos']]

# Crear un diccionario con los nombres antiguos y nuevos
nombres_campos = {'title': 'Nombre', 'type': 'Tipo', 'bookCount': 'Cantidad de libros', 'paperCount': 'Cantidad de artículos', 'numberOfUsersEstimate': 
                  'Cantidad de usuarios', 'numberOfJobsEstimate': 'Cantidad de proyectos', 'githubLanguage_repos': 'Cantidad de repositorios'}

# Renombrar los campos
datos_nuevos = datos_nuevos.rename(columns=nombres_campos)

# Guarda el resultado en un nuevo archivo CSV
datos_nuevos.to_csv('datasource_clean.csv', index=False)

# Leer el archivo CSV en un DataFrame de Pandas
df = pd.read_csv('datasource_clean.csv')

# Reemplazar los valores vacíos con 0
df = df.fillna(value=0)

# Escribir el DataFrame actualizado en un nuevo archivo CSV
df.to_csv('datasource_clean.csv', index=False)

print("Se han eliminado los campos innecesarios")
print("Creado el archivo datasource_clean")
print("")
input("Presione Enter para salir...")