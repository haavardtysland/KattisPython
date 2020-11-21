import sys

number = 0
result = 0
square = 0
n = input()
n = int(n)
for i in range (n):
    number = input()
    number = int(number) 
    square = number % 10
    number = int(number/10)
    result += pow(number, square)
print(result)
