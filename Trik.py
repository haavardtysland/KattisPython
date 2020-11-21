import sys

moves = input()
index = 1
for i in moves:
    if (i == 'A' and index != 3):
        index = 2 if index == 1 else 1
    elif (i == 'B' and index != 1):
        index = 3 if index == 2 else 2
    elif (i == 'C' and index != 2):
        index = 1 if index == 3 else 3


print(index)