from Tablero import Tablero
from Barcos import Barcos


mesa_de_juego = Tablero(8, 8)
mesa_de_juego.mostrar_pantalla()
print('??????????????')
primer_barco = Barcos(3, posicion='hor')
segundo_barco = Barcos(3, posicion='ver')
primer_barco.colocar_barco(2, 3, mesa_de_juego)
segundo_barco.colocar_barco(4, 5, mesa_de_juego)
mesa_de_juego.mostrar_pantalla()