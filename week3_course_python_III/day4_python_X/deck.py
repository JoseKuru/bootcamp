import random

numeros = tuple([x for x in range(1, 11)])
palos = ('picas', 'treboles', 'diamantes', 'corazones')
deck = []
count = 0    
while count < 40:
    a = random.choice(numeros)
    b = random.choice(palos)
    if (a, b) not in deck:
        deck.append((a, b))
        count += 1

deck.sort()
print(deck)
