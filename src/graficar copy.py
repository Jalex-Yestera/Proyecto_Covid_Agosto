# Éste módulo contiene la función que hace el gráfico del json del equipo A @CristiDatas

import pandas as pd
from matplotlib import pyplot as plt


pl=pd.read_json("grupoa.json")
pl.plot()
plt.show()


