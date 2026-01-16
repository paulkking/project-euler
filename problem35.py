from eulertools import checkPrime

out = 1
primes = set()

def checkCirc(n):
    s = str(n)
    p = set()    
    for i in range(len(s)):
        if not checkPrime(int(s)): return False
        s = s[-1] + s[:-1]
        p.add(int(s))
    primes.update(p)
    return True

for i in range(3,1000000,2):
    if i in primes or checkCirc(i):
        out += 1

print(out)