from math import sqrt

out = 0
maxx = 0

for i in range(12,1000):
    s = set()
    for j in range(5,i):
        memo = set()
        for k in range(3,j): # Very slow; O(n^3) time
            l = i - j - k
            if frozenset([j,k,l]) in memo:
                continue
            if l == sqrt(j ** 2 - k ** 2):
                s.add(frozenset([j,k,l]))
            memo.add(frozenset([j,k,l]))
    res = len(s)
    if res > maxx:
        maxx = res
        out = i

print(out)