import pandas as pd
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)

# abrir archivo de demanda actual (nodos_cantidad.csv)
# leer archivo de demanda actual y subirlo a un dataframe
df = pd.read_csv('nodos_cantidad.csv', sep=';')

# abrir el archivo que contiene la totalidad de los nodos en el problema
df_nodos = pd.read_csv('nodos.csv', sep=';')

# crear dataframe de demanda sintetica
df_sintetica = pd.DataFrame(columns=['ID_NODO', 'Cantidad', 'Cantidad/Total'])

# recorrer la lista de nodos existentes
for nodo in df_nodos['ID_NODO']:
    # si el nodo existe en el archivo de demanda actual se indexa ID_NODO y
    # Cantidad en el dataframe de demanda sintetica
    if nodo in df['ID_NODO'].values:
        df_sintetica = df_sintetica.append({'ID_NODO': nodo, 'Cantidad': int(df.loc[df['ID_NODO'] == nodo, 'Cantidad'].values[0])}, ignore_index=True)
    # si el nodo no existe en el archivo de demanda actual se indexa ID_NODO
    else:
        df_sintetica = df_sintetica.append({'ID_NODO': nodo, 'Cantidad': 0}, ignore_index=True)

# medidas de tendencia central de la demanda actual
print('Medidas de tendencia central de la demanda actual')
print('Media: ', df['Cantidad'].mean())
print('Mediana: ', df['Cantidad'].median())
print('Moda: ', df['Cantidad'].mode()[0])
print('Desviación estándar: ', df['Cantidad'].std())
print('Coeficiente de variación: ', df['Cantidad'].std()/df['Cantidad'].mean())

# sumarle x cantidad de demanda a cada nodo
x = 5
df_sintetica['Cantidad'] = df_sintetica['Cantidad'] + x

# calcular Cantidad/Total
df_sintetica['Cantidad/Total'] = df_sintetica['Cantidad']/df_sintetica['Cantidad'].sum()

# medidas de tendencia central de la demanda sintetica
print('Medidas de tendencia central de la demanda sintetica')
print('Media: ', df_sintetica['Cantidad'].mean())
print('Mediana: ', df_sintetica['Cantidad'].median())
print('Moda: ', df_sintetica['Cantidad'].mode()[0])
print('Desviación estándar: ', df_sintetica['Cantidad'].std())
print('Coeficiente de variación: ', df_sintetica['Cantidad'].std()/df_sintetica['Cantidad'].mean())

# guardar el dataframe de demanda sintetica en un archivo csv
df_sintetica.to_csv('nodos_demanda_sintetica.csv', sep=';', index=False)