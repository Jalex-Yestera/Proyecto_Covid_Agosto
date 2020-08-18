# This module is dedicated to all plot functions

# Este módulo contiene la función que hace el gráfico del json del equipo A. @CristiDatas:
# graf
def graf_a(graf):
    pl=pd.read_json(graf)
    pl.plot()
    return plt.show()
graf_a(graf="resources\json\output\grupoa.json")