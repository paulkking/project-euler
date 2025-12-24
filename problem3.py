from eulertools import checkPrime
from math import sqrt

n = 600851475143
out = 0

for i in range(2,int(sqrt(n))+1):
    if n % i == 0:
        if checkPrime(i):
            out = max(out,i)
        if checkPrime(n // i):
            out = max(out,n // i)

print(out)