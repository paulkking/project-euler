from itertools import permutations

l = [[y for y in range(1,x+1)] for x in range(1,10)] # Create lists for 1-digit to max 9-digit number
p = [list(permutations(x)) for x in l] # Create all permutations of ranges

out = []

import math

def checkprime(n):
    if n == 1: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

for x in p:
    for t in x:
        t = int(''.join(str(a) for a in t)) # Convert tuple to integer
        if checkprime(t): out.append(t)

print(max(out))