import sys

text = input()
numOfE = text.count('e')

output = 'h'

for i in range (0, numOfE):
    output += 'ee'

output += 'y'

print(output)