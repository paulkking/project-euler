out = 0

for a in range(1,100):
    for b in range(1,100):
        out = max(out,sum(int(x) for x in str(a ** b)))

print(out)