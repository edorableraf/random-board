import random

board = list()
for x in range(10):
    row = list()
    for y in range(10):
        row.append(random.randint(0,9))
    board.append(row)

def print2DArray(arr):
    for row in arr:
        for num in row:
            print(num, end=" ")
        print()
        
def findSum(arr):
    sum = 0
    for row in arr:
        for num in row:
            sum += num
    return sum
        
print2DArray(board)
print(findSum(board))