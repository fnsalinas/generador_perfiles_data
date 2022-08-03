# In[1]

from pandas_profiling import ProfileReport
from datetime import datetime

from leer_archivos import leer_df

# In[2]
ruta = "/home/ubuntu/workspace/fsalinas/generador_perfiles_data/DATOS.txt"

df = leer_df(ruta, "|", ["id", "nombre", "apellido", "fecha_nacimiento", "direccion", "telefono", "email"])
df.info()
# reporte = ProfileReport()