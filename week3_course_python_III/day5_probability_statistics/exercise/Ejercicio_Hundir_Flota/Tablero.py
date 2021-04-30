import numpy as np

class Tablero:

    def __init__(self, altura, anchura):
        self.altura = altura
        self.anchura = anchura
        self.tabla = [['-' for i in range(self.anchura)] for i in range(self.altura)]

    def mostrar_pantalla(self):
        for i in range(self.altura):
            print(''.join(self.tabla[i]))
        

