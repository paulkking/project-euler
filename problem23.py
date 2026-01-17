from math import sqrt

def isAbund(n):
    s = set()
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
    if sum(s) + 1 > n: return True
    else: return False

abund = set()


for i in range(1,28124):
    if isAbund(i):
        abund.add(i)

nas = set()

for n in abund:
    for m in abund:
        if n + m < 28124:
            nas.add(n + m)
        else:
            break

out = 0

for i in range(1,28124):
    if i not in nas:
        out += i

print(out)