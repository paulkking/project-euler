from eulertools import checkPrime
from math import sqrt

out = 0
idx = 3
primes = set()

def goldbach(n):
    for p in primes:
        sq = sqrt((n - p)/2)
        if sq.is_integer():
            return True
    return False

while out == 0:
    if not checkPrime(idx):
        if goldbach(idx):
            idx +=2
        else:
            out = idx
    else:
        primes.add(idx)
        idx += 2
print(out)