out = 0
for i in range(100,1000):
    for j in range(100,1000):
        res = str(i * j)
        if res == res[::-1]:
            out = max(out,i * j)

print(out)