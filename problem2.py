out = 0

fib_last = 1
fib = 1

while fib <= 4000000:
    fib,fib_last = fib+fib_last,fib
    if fib % 2 == 0:
        out += fib

print(out)