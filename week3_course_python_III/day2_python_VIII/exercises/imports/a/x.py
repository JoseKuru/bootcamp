import sys, os

ruta_x = __file__
for i in range(2):
    ruta_x = os.path.dirname(ruta_x)
    sys.path.append(ruta_x)

import b.c.z as z

def f1x():
    print(f1x.__name__)

def f2x():
    print(f2x.__name__)
    # z.f2z() Añadir esta llamada da error porque entra en un bucle recursivo

x1 = 2
x2 = 4

if __name__ == '__main__':
    f1x()
    print('-------')
    f2x()