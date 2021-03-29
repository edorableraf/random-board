import random

board = []
for i in range(10):
    board.append([])
    for j in range(10):
        board[i].append(random.randint(0,9))

for row in board:
    for num in row:
        print(num, end=" ")
    print()