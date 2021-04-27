import sys, os

ruta_y = __file__
for i in range(2):
    ruta_y = os.path.dirname(ruta_y)
    sys.path.append(ruta_y)

import a.x as x

def f1y():
    print(f1y.__name__)
    x.f1x()

def f2y():
    print(f2y.__name__)
    x.f2x()

y1 = 5
y2 = 25

if __name__ == '__main__':
    f1y()
    print('-------')
    f2y()