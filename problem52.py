from collections import Counter

def check6x(n):
    cnt = Counter(str(n))
    for i in range(2,7):
        if Counter(str(n*i)) != cnt:
            return False
    return True

out = 0
idx = 0

while out == 0:
    idx += 1
    if check6x(idx):
        out = idx

print(idx)