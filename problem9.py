from math import sqrt

def checkTrip(a,b,c):
    return a ** 2 + b ** 2 == c ** 2

out = 0

for c in range(2,1001):
    for a in range(2,c):
        b = int(sqrt(c ** 2 - a ** 2))
        if checkTrip(a,b,c) and a + b + c == 1000:
            out = a * b * c

print(out)