# Importamos la librería ctypes
import ctypes

# Cargamos la libreria 
libaddToGINI = ctypes.CDLL('./libaddToGINI.so')

# Definimos los tipos de los argumentos de la función factorial
libaddToGINI.add_one.argtypes = (ctypes.c_float,)

# Definimos el tipo del retorno de la función factorial
libaddToGINI.add_one.restype = (ctypes.c_float)
# Creamos nuestra función factorial en Python
# hace de Wrapper para llamar a la función de C

def add_one(num):
    return libaddToGINI.add_one(num)  
