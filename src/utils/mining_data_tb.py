# Module dedicated to data wrangling functions
import pandas as pd

# Función para seleccionar los países a analizar:
def seleccion_paises(dataframe,paises):
    dataframe=dataframe.loc[dataframe["location"].isin(paises)]
    return dataframe

# Función para seleccionar las columnas a analizar:
def seleccion_columnas(dataframe,col1,col2):
    dataframe=dataframe.iloc[:,col1:col2]
    return dataframe

# Función para buscar cuándo fue el primer caso y borrar las fechas anteriores. Tomamos su índice y el del último caso y actualizamos df. Se actualizará en cada carga.
def borrar_previo(dataframe):
    nuevos_casos=dataframe.pivot_table("new_cases", index='date',columns='location')
    nuevos_casos=nuevos_casos[nuevos_casos>0]
    primer_caso=str(nuevos_casos.first_valid_index().date())
    ultimo_valor=str(dataframe.last_valid_index().date())
    dataframe=dataframe.loc[primer_caso:ultimo_valor]
    return dataframe

# Función para cambiar los valores Nan por ceros:
def cero_nan(dataframe):
    dataframe=dataframe.fillna(0)
    return dataframe



