def lychrel(n):
    for i in range(50):
        n += int(str(n)[::-1])
        if str(n) == str(n)[::-1]:
            return False
    return True

out = 0

for i in range(1,10000):
    if lychrel(i): out += 1

print(out)