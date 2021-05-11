import os, sys

def limpiar_terminal():
    '''
    Esta función limpia la terminal de cualquier informacion aterior
    No recibe argumentos
    Retorna None'''

    os.system('clear')

def subir_carpeta(numero_subidas : int):
    '''
    Esta funcion agrega al path la n subida de carpeta desde el fichero actual
    Args:
        numero_subidas[int] = Número de veces que se subira de carpeta
    Return:
        None'''
    
    ruta = os.getcwd()
    for i in range(numero_subidas):
        ruta = os.path.dirname(ruta)
    sys.path.append(ruta)