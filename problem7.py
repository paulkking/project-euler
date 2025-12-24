from eulertools import checkPrime

idx = 0
p = 1

while idx < 10001:
    p += 1
    if checkPrime(p):
        idx += 1
    
print(p)