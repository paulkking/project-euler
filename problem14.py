memo = dict()

def collatz(n):
    if n == 1:
        return 1
    elif n in memo:
        return memo[n]
    elif n % 2 == 0:
        return 1 + collatz(n / 2)
    else:
        return 1 + collatz(n * 3 + 1)
    
l = 0
out = 0

for i in range(1,1000000):
    res = collatz(i)
    memo[i] = res
    if res > l:
        l = res
        out = i

print(out)