import numpy as np
from os import system, name

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
def board(num1, num2):
    x = np.ones((10, 10))
    #x[1:-1, 1:-1] = 0
    print("Num1: " + str(num1))
    print("Num2: " + str(num2))
    if num1 > 9 or num2 > 9:
        print("Move is out of range")
        print(exit)
        exit()
    else:
        x[num1, num2] = 0
        print(x)
def move():
    move = input("type up, down, left or right: ").lower()
    return move

num1 = 5
num2 = 5    
print("Welcome to the board, I am Robot")
print("You can move up, down, left or right")

var = 1
while var == 1: 
    clear()
    board(num1, num2)
    direction = move()
    print("Move = " + direction)
    if direction == "up":
        num1 -= 1
        board(num1, num2)
    elif direction == "down":
        num1 += 1
        board(num1, num2)
    elif direction == "left":
        num2 -= 1
        board(num1, num2)
    elif direction == "right":
        num2 += 1
        board(num1, num2)
    else:
        board(num1, num2)
        var = 2
        print(exit)
        exit()
