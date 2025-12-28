from eulertools import checkPrime

def checkTrunk(n):
    if not checkPrime(n): return False
    s = str(n)
    for i in range(1,len(s)):
        if not checkPrime(int(s[i:])) or not checkPrime(int(s[:-i])):
            return False
    return True

t = []
idx = 11

while len(t) < 11:
    if checkTrunk(idx):
        t.append(idx)
    idx += 1

print(sum(t))