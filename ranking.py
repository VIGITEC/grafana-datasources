import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('datasource_clean.csv')

# Seleccionar solo las columnas numéricas
num_cols = df.select_dtypes(include='number').columns

# Agregar una columna con la suma de los valores numéricos
df['Total'] = df[num_cols].sum(axis=1)

# Ordenar el DataFrame por la columna 'Total' en orden descendente
df = df.sort_values('Total', ascending=False)

# Escribir el DataFrame ordenado en un nuevo archivo CSV
df.to_csv('datasource_updated.csv', index=False)

print("Se ha establecido el ranking")
print("Creado el archivo datasource_updated")
print("")
input("Presione Enter para salir...")