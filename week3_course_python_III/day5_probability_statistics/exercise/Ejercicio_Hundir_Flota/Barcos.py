class Barcos:

    def __init__(self, nombre, largo):
        
        self.nombre = nombre
        self.largo = largo
        self.orientacion = None
        self.posicion = []
        self.vida = largo


    def colocar_barco(self, coordenada_y, coordenada_x, Tablero):
        if self.orientacion == 'h':
            for i in range(len(Tablero.tabla[coordenada_y])):
                if i in [x for x in range(coordenada_x, coordenada_x + self.largo)]:
                    self.posicion.append((coordenada_y, i))
                    Tablero.tabla[coordenada_y][i] = '#'
        
        if self.orientacion == 'v':
            for i in range(len(Tablero.tabla)):
                if i in [x for x in range(coordenada_y, coordenada_y + self.largo)]:
                    self.posicion.append((i, coordenada_x))
                    Tablero.tabla[i][coordenada_x] = '#'         
    
    def establecer_orientacion(self, orientacion):
        self.orientacion = orientacion