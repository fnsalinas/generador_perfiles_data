# In[1]

from typing import Dict, List, Tuple, Any
from pandas_profiling import ProfileReport
from datetime import datetime

from leer_archivos import leer_df

# In[2]
reports = "/home/ubuntu/workspace/fsalinas/generador_perfiles_data/reports"
ruta = "/home/ubuntu/workspace/fsalinas/generador_perfiles_data/DATOS.txt"

df = leer_df(ruta, "|")
df.info()
reporte = ProfileReport(df, title="Reporte de datos", minimo = True)

reporte.to_file("/home/ubuntu/workspace/fsalinas/generador_perfiles_data/reporte_datos.html")