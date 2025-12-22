from eulertools import checkPrime

primes = []
m = 1000000

for i in range(m):
    if checkPrime(i):
        primes.append(i)

out = 0
n = 0
primeset = set(primes)

for i in range(len(primes)):
    summ = 0
    for j in range(i,len(primes)):
        summ += primes[j]
        if summ >= m: break
        if summ in primeset and j-i+1 > n:
            n = j-i+1
            out = summ

print(out)