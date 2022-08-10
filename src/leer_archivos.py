# %%

from typing import Dict, List, Tuple, Any
import pandas as pd

# %%

def leer_df(ruta_archivo: str, sep: str, encabezados: List[str] = None) -> pd.DataFrame:
    """
    Esta es una función que lee archivos y devuelve un dataframe de pandas

    Args:
        ruta_archivo (str): Ruta completa al archivo que se desea leer
        sep (str): Caracter separador de campos por fila
        encabezados (List[str]): Lista de nombres de los encabezados del archivo,
                                 si no se envía un valor, se tomarán los encabezados
                                 del archivo

    Returns:
        df (pandas.DataFrame): Dataframe que contiene toda la data del archivo leido
    """
    if encabezados:
        df = pd.read_csv(ruta_archivo, sep = sep, header=None, names=encabezados)
    else:
        df = pd.read_csv(ruta_archivo, sep = sep)

    filas, columnas = df.shape

    print("El dataframe tiene {x} fila(s) y {y} columna(s)".format(x=filas, y=columnas))

    return df