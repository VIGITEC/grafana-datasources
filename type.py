import pandas as pd

# Cargar el archivo CSV en un DataFrame de pandas
df = pd.read_csv('datasource_updated.csv')
df1 = pd.read_csv('datasource_updated.csv')
df2 = pd.read_csv('datasource_updated.csv')
df3 = pd.read_csv('datasource_updated.csv')
df4 = pd.read_csv('datasource_updated.csv')
df5 = pd.read_csv('datasource_updated.csv')
df6 = pd.read_csv('datasource_updated.csv')
df7 = pd.read_csv('datasource_updated.csv')
df8 = pd.read_csv('datasource_updated.csv')
df9 = pd.read_csv('datasource_updated.csv')
df10 = pd.read_csv('datasource_updated.csv')
df11 = pd.read_csv('datasource_updated.csv')
df12 = pd.read_csv('datasource_updated.csv')
df13 = pd.read_csv('datasource_updated.csv')
df14 = pd.read_csv('datasource_updated.csv')
df15 = pd.read_csv('datasource_updated.csv')
df16 = pd.read_csv('datasource_updated.csv')
df17 = pd.read_csv('datasource_updated.csv')
df18 = pd.read_csv('datasource_updated.csv')
df19 = pd.read_csv('datasource_updated.csv')
df20 = pd.read_csv('datasource_updated.csv')
df21 = pd.read_csv('datasource_updated.csv')
df22 = pd.read_csv('datasource_updated.csv')
df23 = pd.read_csv('datasource_updated.csv')
df24 = pd.read_csv('datasource_updated.csv')

# Mantener solo las filas donde el valor de la columna "Nombre" sea "Juan"
df = df[df['Tipo'] == 'pl']
df1 = df1[df1['Tipo'] == 'library']
df2 = df2[df2['Tipo'] == 'framework']
df3 = df3[df3['Tipo'] == 'queryLanguage']
df4 = df4[df4['Tipo'] == 'application']
df5 = df5[df5['Tipo'] == 'os']
df6 = df6[df6['Tipo'] == 'dataNotation']
df7 = df7[df7['Tipo'] == 'assembly']
df8 = df8[df8['Tipo'] == 'stylesheetLanguage']
df9 = df9[df9['Tipo'] == 'textMarkup']
df10 = df10[df10['Tipo'] == 'protocol']
df11 = df11[df11['Tipo'] == 'grammarLanguage']
df12 = df12[df12['Tipo'] == 'template']
df13 = df13[df13['Tipo'] == 'cloud']
df14 = df14[df14['Tipo'] == 'xmlFormat']
df15 = df15[df15['Tipo'] == 'editor']
df16 = df16[df16['Tipo'] == 'idl']
df17 = df17[df17['Tipo'] == 'jsonFormat']
df18 = df18[df18['Tipo'] == 'contract']
df19 = df19[df19['Tipo'] == 'compiler']
df20 = df20[df20['Tipo'] == 'notation']
df21 = df21[df21['Tipo'] == 'packageManager']
df22 = df22[df22['Tipo'] == 'schema']
df23 = df23[df23['Tipo'] == 'isa']
df24 = df24[df24['Tipo'] == 'hardwareDescriptionLanguage']
df24 = df24[df24['Tipo'] == 'barCodeFormat']

# Guardar el nuevo DataFrame en un nuevo archivo CSV
df.to_csv('pldb_pl.csv', index=False)
df1.to_csv('pldb_library.csv', index=False)
df2.to_csv('pldb_framework.csv', index=False)
df3.to_csv('pldb_sql.csv', index=False)
df4.to_csv('pldb_app.csv', index=False)
df5.to_csv('pldb_os.csv', index=False)
df15.to_csv('pldb_editor.csv', index=False)

print("Se han creado los nuevos archivos CSV")
print("")
input("Presione Enter para salir...")