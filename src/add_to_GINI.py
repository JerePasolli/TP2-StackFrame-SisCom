# Importamos la librería ctypes
import ctypes

# Cargamos la libreria 
libaddToGINI = ctypes.CDLL('./lib/libaddToGINI.so')

# Definimos los tipos de los argumentos de la función
libaddToGINI.add_one.argtypes = (ctypes.c_float,)

# Definimos el tipo del retorno de la función
libaddToGINI.add_one.restype = (ctypes.c_int)

# hace de Wrapper para llamar a la función de C

def add_one(num):
    return libaddToGINI.add_one(num)  
