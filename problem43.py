from itertools import permutations

l = list(permutations(range(0,10)))

def fn(n):
    s = str(n)
    p = (2,3,5,7,11,13,17)
    for i in range(7):
        if int(s[i+1:i+4]) % p[i] != 0:
            return False
    return True

out = 0

for perm in l:
    if perm[0] == 0: continue
    num = int("".join([str(x) for x in perm]))
    if fn(num):
        out += num

print(out)