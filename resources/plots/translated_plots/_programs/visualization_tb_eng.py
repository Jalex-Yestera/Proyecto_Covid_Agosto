# This module is dedicated to all plot functions

import pandas as pd
import matplotlib.pyplot as plt

# Función que hace el gráfico del json del equipo A: @CristiDatas

def graf_a(graf):
    pl=pd.read_json(graf)
    pl.plot()
    plt.show()
#graf_a(graf="resources\json\output\grupoa.json")

# Función paises_juntos para comparar la evolución a lo largo del tiempo de cada columna en todos los países del grupo a la vez. Primero hace una pivot table de cada columna, luego muestra cada gráfico y por último los guarda como archivos en la carpeta paises_juntos, de plots, dentro de resources. La función toma como parámetros el dataframe que analizamos y el diccionario con los colores que usamos para cada país. Cada vez que se ejecuta sobreescribe el archivo para actualizar. @CristiDatas

def paises_juntos(dataframe,colores_paises):
    val=dataframe.columns[1:]
    for v in val:
        print("\n",v,"\n")
        paises=dataframe.pivot_table(values=v, index='date',columns='location',fill_value=0)
        paises.plot(color=colores_paises.values())
        plt.title(v)
        plt.show()
    for v in val:
        paises=dataframe.pivot_table(values=v, index='date',columns='location',fill_value=0)
        paises.plot()
        paises.plot(color=colores_paises.values())
        plt.title(v)
        plt.savefig("../resources/plots/paises_juntos/"+v+".png")
        plt.close()

# Función paises_juntos_mes: igual que función paises_juntos pero cambiando la frecuencia a mensual y haciendo una media aritmética de esos  valores, con lo que los outliers provocados por los ajustes quedan repartidos entre el resto de los datos y las curvas se suavizan. Cada gráfico se muestra en pantalla y luego se guarda en la misma carpeta de paises_juntos pero agregando el sufijo "_mes" . @CristiDatas

def paises_juntos_mes(dataframe,colores_paises):
    val=dataframe.columns[1:]
    for v in val:
        print("\n",v,"\n")
        paises=dataframe.pivot_table(values=v, index='date',columns='location',fill_value=0)
        paises=paises.resample("M").mean()
        paises.plot(color=colores_paises.values())
        plt.title(v+" - MONTHLY EVOLUTION ")
        plt.show()
    for v in val:
        paises=dataframe.pivot_table(values=v, index='date',columns='location',fill_value=0)
        paises=paises.resample("M").mean()
        paises.plot(color=colores_paises.values())
        plt.title(v+" - MONTHLY EVOLUTION")
        plt.savefig("../resources/plots/paises_juntos/"+v+"_mes.png")
        plt.close()
        
# Función emergencias para ver las diferentes tendencias de cada columna para cada país. Se muestra verticalmente el inicio y el fin del estado de alarme (si lo hay). Para ello usamos las columnas d¡seleccionadas como una lista que recorrremos y dentro de ésta usamos la pivot table de paises_juntos para recorrer cada país. Para las líneas verticales usamos una lista con las fechas de los estados de emergencia (que hemos documentado en documentation) y la recorremos para trazar las líneas y el título. Primero muestra cada gráfico agrupados por columnas y después por países y después guarda los gráficos de cada país en su carpeta correspondiente dentro de la carpeta plots de resources. La función toma como parámetros el dataframe que analizamos, las fechas de emergencia y el diccionario con los colores que usamos para cada país. Cada vez que se ejecuta sobreescribe los archivos para actualizar. @CristiDatas

def emergencias(dataframe,emergencia,colores_paises):
    val=dataframe.columns[1:]
    for v in val:
        print("\n",v,"\n")
        paises_juntos=dataframe.pivot_table(values=v, index='date',columns='location',fill_value=0)
        locat=paises_juntos.columns
        for x,l in enumerate(locat):
            print("\n",l,"\n")
            pais=paises_juntos[l]
            pais.plot(color=colores_paises[l])
            for e in emergencia[x]:
                plt.axvline(x=e, animated=True, lw=4, color="yellow",label=e, linestyle="--")
                plt.legend()
            plt.axvline()
            plt.title(l+":  "+v+"\nAlarm state activated on "+emergencia[x][0])
            plt.show()
        for x,l in enumerate(locat):
            pais=paises_juntos[l]
            pais.plot(color=colores_paises[l])
            for e in emergencia[x]:
                plt.axvline(x=e, animated=True, lw=4, color="yellow",label=e, linestyle="--")
                plt.legend()
            plt.axvline()
            plt.title(l+":  "+v+"\nAlarm state activated on "+emergencia[x][0])
            plt.savefig("../resources/plots/"+l+"/"+l+"_"+v+".png")
            plt.close()

# Función emergencias_mes: igual que función emergencias pero cambiando la frecuencia a mensual y haciendo una media aritmética de esos  valores, con lo que los outliers provocados por los ajustes quedan repartidos entre el resto de los datos y las curvas se suavizan. Cada gráfico se muestra en pantalla y luego se guarda en la carpeta correspondiente a su país pero agregando el sufijo "_mes" . @CristiDatas

def emergencias_mes(dataframe,emergencia,colores_paises):
    val=dataframe.columns[1:]
    for v in val:
        print("\n",v,"\n")
        paises_juntos=dataframe.pivot_table(values=v, index='date',columns='location',fill_value=0)
        paises_juntos=paises_juntos.resample("M").mean()
        locat=paises_juntos.columns
        for x,l in enumerate(locat):
            print("\n",l,"\n")
            pais=paises_juntos[l]
            pais.plot(color=colores_paises[l])
            for e in emergencia[x]:
                plt.axvline(x=e, animated=True, lw=4, color="yellow",label=e, linestyle="--")
                plt.legend()
            plt.axvline()
            plt.title(l+":  "+v+" - MONTHLY EVOLUTION \nAlarm state activated on "+emergencia[x][0])
            plt.show()
        for x,l in enumerate(locat):
            pais=paises_juntos[l]
            pais.plot(color=colores_paises[l])
            for e in emergencia[x]:
                plt.axvline(x=e, animated=True, lw=4, color="yellow",label=e, linestyle="--")
                plt.legend()
            plt.axvline()
            plt.title(l+":  "+v+" - MONTHLY EVOLUTION \nAlarm state activated on "+emergencia[x][0])
            plt.savefig("../resources/plots/"+l+"/"+l+"_"+v+".png")
            plt.close()

# Función total_paises para comprobar el puesto de España respecto al resto de los países en cuanto al total de muertos y casos (absolutos y por millón de habitantes). La función toma como parámetros el dataframe a analizar, las columnas que vamos a analizar (en este caso las referentes a localización y totales) y el diccionario con los colores correspondientes a cada país. Recorremos las columnas con un for, hacemos una pivot table para cada valor y seleccionamos el penúltimo (porque hemos comprobado que el último registro a veces contiene valores nulos porque no se tienen datos actualizados). La función primero muestra cada uno de los gráficos y después los guarda en la carpeta paises_juntos dentro de la carpeta plots de resources añadiendo el prefijo "barras_" y el nombre de cada columna analizada. @CristiDatas

def total_paises(dataframe,cols,colores_paises):
    totales=dataframe.iloc[:,cols]
    val=totales.columns[1:]
    for v in val:
        print("\n",v,"\n")
        tot=totales.pivot_table(values=v, index='date',columns='location',fill_value=0)
        tot=(tot.iloc[-2])
        tot.plot(kind="bar",width=0.8,color=colores_paises.values())
        plt.title(v)
        plt.xticks(rotation=45)
        plt.show()
    for v in val:
        tot=totales.pivot_table(values=v, index='date',columns='location',fill_value=0)
        tot=(tot.iloc[-2])
        tot.plot(kind="bar",width=0.8,color=colores_paises.values())
        plt.title(v)
        plt.xticks(rotation=45)
        plt.savefig("../resources/plots/paises_juntos/barras_"+v+"_.png")
        plt.close()

# Función total_paises_orden: igual que la función totales_paises pero ordenando los países de forma descendente. Al estandarizar la función se pierde el color específico de cada país pero las posiciones de cada uno quedan más claras. Primero muestra cada gráfico y después los guarda en la carpeta paises_juntos dentro de la carpeta plots de resources añadiendo el prefijo "barras_orden_" y el nombre de cada columna analizada. @CristiDatas

def total_paises_orden(dataframe,cols):
    totales=dataframe.iloc[:,cols]
    val=totales.columns[1:]
    for v in val:
        print("\n",v,"\n")
        tot=totales.pivot_table(values=v, index='date',columns='location',fill_value=0)
        tot=(tot.iloc[-2])
        tot=tot.sort_values(ascending=False)
        tot.plot(kind="bar",width=0.8, color="rosybrown")
        plt.title(v)
        plt.xticks(rotation=45)
        plt.show()
    for v in val:
        tot=totales.pivot_table(values=v, index='date',columns='location',fill_value=0)
        tot=(tot.iloc[-2])
        tot=tot.sort_values(ascending=False)
        tot.plot(kind="bar",width=0.8, color="rosybrown")
        plt.title(v)
        plt.xticks(rotation=45)
        plt.savefig("../resources/plots/paises_juntos/barras_orden_"+v+"_.png")
        plt.close()