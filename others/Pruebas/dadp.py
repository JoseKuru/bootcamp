import random
from matplotlib import pyplot as pt

class ndado():
    
    def __init__(self, nfaces):
        self.nfaces = nfaces
        self.valor = self.roll()

    def roll(self):
        return random.randint(1, self.nfaces)

    def __str__(self):
        return f'Soy un dado de {self.nfaces}, me lanzaaaaaaaaan y un {self.valor}!'

dado_seis = ndado(6)
lista_num = [x for x in range(1, 7)]
lista_pro = [0 for x in range(6)]
lista_squares = [x ** 2 for x in range(1, 7)]
for i in range(100000):
    a = random.randint(1, 6)
    lista_pro[a-1] += 1
pt.bar(lista_num, lista_pro, color='cyan')
pt.scatter(lista_num, lista_squares)
pt.show()