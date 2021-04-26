import random

def print_board():
    for row in board:
        print(' '.join(row))

board = [['0' for i in range(5)] for i in range(5)]
x, y = random.randint(0, 5), random.randint(0, 5)
print_board()

while True:
    row_in = int(input('Introduce el número de la fila: '))
    col_in = int(input('Introduce el número de la columna: '))
    board[row_in - 1][col_in - 1] = '*'
    print_board()
    if board[row_in - 1][col_in - 1] == board[x][y]:
        break

print('YOOOOOOOU WIIIIIN')