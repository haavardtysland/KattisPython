import sys

result = 0
n, h, v = input().split()
n = int(n)
h = int(h)
v = int(v)

result = (n - h if n > h else h)*(n - v if n > v else v)*4
print(result)