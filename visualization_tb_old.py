# This module is dedicated to all plot functions
<<<<<<< HEAD
# Éste módulo contiene la función que hace el gráfico del json del equipo A @CristiDatas
# graf
=======

import pandas as pd
import matplotlib.pyplot as plt

# Función que hace el gráfico del json del equipo A: @CristiDatas

>>>>>>> 1ad3f0f3ced4f318e966262e92c6080b66618798
def graf_a(graf):
    pl=pd.read_json(graf)
    pl.plot()
    plt.show()
#graf_a(graf="resources\json\output\grupoa.json")

# Función paises_juntos para comparar la evolución a lo largo del tiempo de cada columna en todos los países del grupo a la vez. Primero hace una pivot table de cada columna, luego muestra cada gráfico y por último los guarda como archivos en la carpeta paises_juntos, de plots, dentro de resources. Cada vez que se ejecuta sobreescribe el archivo para actualizar. @CristiDatas

def paises_juntos(dataframe):
    colores_paises = ["#1f77b4","#d62728","#8c564b","#2ca02c","#bcbd22"]
    val=dataframe.columns[1:]
    for v in val:
        print("\n",v,"\n")
        paises=dataframe.pivot_table(values=v, index='date',columns='location',fill_value=0)
        paises.plot(color=colores_paises)
        plt.title(v)
        plt.show()
    for v in val:
        print("\n",v,"\n")
        paises=dataframe.pivot_table(values=v, index='date',columns='location',fill_value=0)
        paises.plot()
        paises.plot(color=colores_paises)
        plt.title(v)
        plt.savefig("../resources/plots/paises_juntos/"+v+".png")
        plt.close()
        


