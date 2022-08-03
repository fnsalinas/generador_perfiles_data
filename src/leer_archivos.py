import pandas as pd

def leer_df(ruta_archivo, sep, encabezados):
    df = pd.read_csv(ruta_archivo, sep = sep, header=None, names=encabezados)
    return df