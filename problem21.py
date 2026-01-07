from math import sqrt

def pSum(n):
    div = set()
    for i in range(1,int(sqrt(n))+1):
        if n % i == 0:
            div.add(i)
            div.add(n // i)
    return sum(x for x in div if x < n)

d = dict()
out = 0

for i in range(1,10000):
    d[i] = pSum(i)

for x,y in d.items():
    if x != y and y in d and d[y] == x:
        out += y

print(out)