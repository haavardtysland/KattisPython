import sys

number = input()

bitvalue = format(int(number), 'b')
newbitvalue = bitvalue [::-1]

print(int(newbitvalue, 2))
