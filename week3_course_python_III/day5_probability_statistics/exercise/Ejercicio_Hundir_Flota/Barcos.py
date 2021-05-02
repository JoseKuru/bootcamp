class Barcos:

    def __init__(self, nombre, largo):
        
        self.nombre = nombre
        self.largo = largo
        self.orientacion = None
        self.posicion = []
        self.vida = largo


    def colocar_barco(self, coordenada_y, coordenada_x, Tablero, lista_posiciones):
        if coordenada_y == 0 or coordenada_y > 10 or coordenada_x == 0 or coordenada_x > 10:
            raise Exception('Fuera de rango')

        if self.orientacion == 'h':
            for i in range(len(Tablero.tabla[coordenada_y])):
                if i in [x for x in range(coordenada_x, coordenada_x + self.largo)]: # Igual se pude unir a la linea de arriba?
                    if i + coordenada_x > 10 or (coordenada_y, i) in lista_posiciones or (coordenada_y, i+1) in lista_posiciones or (coordenada_y, i+2) in lista_posiciones or (coordenada_y, i+3) in lista_posiciones or (coordenada_y, i+4) in lista_posiciones: #MUY Mal
                        self.posicion = []
                        raise Exception('Fuera de rango/ Los barcos han chocado')                       
                    self.posicion.append((coordenada_y, i))
                    Tablero.tabla[coordenada_y][i] = '#'
        
        if self.orientacion == 'v':
            for i in range(len(Tablero.tabla)):
                if i in [x for x in range(coordenada_y, coordenada_y + self.largo)]:
                    if i + coordenada_y > 10:
                        raise Exception('Fuera de rango')
                    self.posicion.append((i, coordenada_x))
                    Tablero.tabla[i][coordenada_x] = '#'         
    
    def establecer_orientacion(self, orientacion):
        self.orientacion = orientacion