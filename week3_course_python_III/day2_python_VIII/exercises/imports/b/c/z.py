import sys, os

ruta_z = __file__
for i in range(3):
    ruta_z = os.path.dirname(ruta_z)
    sys.path.append(ruta_z)

import a.x as x
import b.y as y

def f1z():
    print(f1z.__name__)
    y.f1y()

def f2z():
    print(f2z.__name__)
    x.f2x()

z1 = 10
z2 = 100

if __name__ == '__main__':
    f1z()
    print('-------')
    f2z()