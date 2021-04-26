import numpy as np

board = [[0 for i in range(9)] for i in range(9)]

def print_board():
    for i in range(len(board)):
        print('')
        if i % 3 == 0 and i != 0:
            print('-------------------')
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print('|', end='')
            print(board[i][j], end=' ')

def isPossible(board, x, y, e):
    for i in range(len(board[x])):
        if x == board[y][i]:
            return False
    for i in range(len(board)):
        if y == board[i][x]:
            return False
    box_x = x // 3
    box_y = y // 3
    



print_board()
            