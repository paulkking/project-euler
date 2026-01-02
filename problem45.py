out = 0
hidx = 143
tidx = 285
pidx = 165

def tNum(n):
    return n * (n + 1) // 2

def pNum(n):
    return n * (3 * n - 1) // 2

def hNum(n):
    return int(n * (2 * n - 1))

while out == 0:
    hidx += 1
    h = hNum(hidx)
    while h > tNum(tidx):
        tidx += 1
    while h > pNum(pidx):
        pidx += 1    
    if h == tNum(tidx) and h == pNum(pidx):
        out = h

print(out)