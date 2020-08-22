# This module is dedicated to all plot functions

import pandas as pd
import matplotlib.pyplot as plt

# Función que hace el gráfico del json del equipo A: @CristiDatas

def graf_a(graf):
    pl=pd.read_json(graf)
    pl.plot()
    plt.show()
#graf_a(graf="resources\json\output\grupoa.json")

# Función paises_juntos para comparar la evolución a lo largo del tiempo de cada columna en todos los países del grupo a la vez. Primero hace una pivot table de cada columna, luego muestra cada gráfico y por último los guarda como archivos en la carpeta paises_juntos, de plots, dentro de resources. La función toma como parámetros el dataframe que analizamos y la lista con los colores que usamos para cada país. Cada vez que se ejecuta sobreescribe el archivo para actualizar. @CristiDatas

def paises_juntos(dataframe,colores_paises):
    colores_paises = ["dodgerblue","red","g","magenta","darkorange"]
    val=dataframe.columns[1:]
    for v in val:
        print("\n",v,"\n")
        paises=dataframe.pivot_table(values=v, index='date',columns='location',fill_value=0)
        paises.plot(color=colores_paises)
        plt.title(v)
        plt.show()
    for v in val:
        paises=dataframe.pivot_table(values=v, index='date',columns='location',fill_value=0)
        paises.plot()
        paises.plot(color=colores_paises)
        plt.title(v)
        plt.savefig("../resources/plots/paises_juntos/"+v+".png")
        plt.close()

# Función emergencias para ver las diferentes tendencias de cada columna para cada país. Se muestra verticalmente el inicio y el fin del estado de alarme (si lo hay). Para ello usamos las columnas d¡seleccionadas como una lista que recorrremos y dentro de ésta usamos la pivot table de paises_juntos para recorrer cada país. Para las líneas verticales usamos una lista con las fechas de los estados de emergencia (que hemos documentado en documentation) y la recorremos para trazar las líneas y el título. Primero muestra cada gráfico agrupados por columnas y después por países y después guarda los gráficos de cada país en su carpeta correspondiente dentro de la carpeta plots de resources. La función toma como parámetros el dataframe que analizamos, las fechas de emergencia y la lista con los colores que usamos para cada país. Cada vez que se ejecuta sobreescribe los archivos para actualizar. @CristiDatas

def emergencias(dataframe,emergencia,colores_paises):
    val=dataframe.columns[1:]
    for v in val:
        print("\n",v,"\n")
        paises_juntos=dataframe.pivot_table(values=v, index='date',columns='location',fill_value=0)
        locat=paises_juntos.columns
        for x,l in enumerate(locat):
            print("\n",l,"\n")
            pais=paises_juntos[l]
            pais.plot(color=colores_paises[x])
            for e in emergencia[x]:
                plt.axvline(x=e, animated=True, lw=4, color="yellow",label=e, linestyle="--")
                plt.legend()
            plt.axvline()
            plt.title(l+":  "+v+"\nEstado de emergencia decretado el "+emergencia[x][0])     
            plt.show()
        for x,l in enumerate(locat):
            pais=paises_juntos[l]
            pais.plot(color=colores_paises[x])
            for e in emergencia[x]:
                plt.axvline(x=e, animated=True, lw=4, color="yellow",label=e, linestyle="--")
                plt.legend()
            plt.axvline()
            plt.title(l+":  "+v+"\nEstado de emergencia decretado el "+emergencia[x][0])
            plt.savefig("../resources/plots/"+l+"/"+l+"_"+v+".png")
            plt.close()