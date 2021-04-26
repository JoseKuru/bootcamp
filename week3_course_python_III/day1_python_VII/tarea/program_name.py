board = [['|' if i%2==0 else '_' for i in range(17)] for i in range(8)]
for row in board:
    print(''.join(row))