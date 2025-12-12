l = []
left = 1 / 3
right = 1 / 2

def gcd(n,d):
    while n != 0:
        d , n = n, d % n
    return d

for i in range(1,12001):
    for j in range(max(1,i // 3 - 1),i // 2 + 2):
        if j / i > left and j / i < right and gcd(i,j) == 1:
            l.append((j,i))

print(len(l))