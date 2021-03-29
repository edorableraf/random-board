import random

board = []
for i in range(10):
    board.append([])
    for j in range(10):
        board[i].append(random.randint(0,9))

for row in board:
    line = ""
    for num in row:
        line += "{} ".format(num)
    print(line)