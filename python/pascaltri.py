from math import *
def pascalRow(n):
    L = []
    for i in range(n+1):
        L += [factorial(n) / (factorial(i) * factorial(n - i))]
    print(L)

def pascal(n):
    for i in range(n):
        pascalRow(i)

pascal(12)
