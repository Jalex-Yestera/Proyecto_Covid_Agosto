# This that contains the generic functionality related to open, create, read and write files.
import pandas as pd

# Función para abrir el dataset. Convertimos el csv en dataframe csv_df y establecemos que "date" es tipo fecha:
def open_csv(url):
    csv_df=pd.read_csv(url, parse_dates=["date"], index_col="date")
    return csv_df