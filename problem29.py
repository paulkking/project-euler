s = set()

a = 100
b = 100

for i in range(2,a+1):
    for j in range(2,b+1):
        s.add(i ** j)

print(len(s))