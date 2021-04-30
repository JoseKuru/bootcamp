class Barcos:

    def __init__(self, largo, posicion):
        
        self.largo = largo
        self.posicion = posicion

    def colocar_barco(self, coordenada_x, coordenada_y, Tablero):
        if self.posicion == 'hor':
            for i in range(len(Tablero.tabla[coordenada_y])):
                if i in [x for x in range(coordenada_x, coordenada_x + self.largo)]:
                    Tablero.tabla[coordenada_y][i] = 'O'
        
        if self.posicion == 'ver':
            for i in range(len(Tablero.tabla)):
                if i in [x for x in range(coordenada_y, coordenada_y + self.largo)]:
                    Tablero.tabla[i][coordenada_x] = 'O'