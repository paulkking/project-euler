from eulertools import checkPrime

out = 0

n = 2000000

for i in range(2,n):
    if checkPrime(i):
        out += i

print(out)