from math import sqrt

out = 0
tri = 1
idx = 1

while out == 0:
    factors = set()
    for i in range(1,int(sqrt(tri)+1)):
        if tri % i == 0:
            factors.add(i)
            factors.add(tri / i)
    if len(factors) > 500:
        out = tri
    else:
        idx += 1
        tri += idx

print(out)