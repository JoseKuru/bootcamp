board = [['|' if i%2==0 and x!=0 else ' ' if i%2==0 and x==0 else '_' for i in range(17)] for x in range(9)]
for row in board:
    print(''.join(row))