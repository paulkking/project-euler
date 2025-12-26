out = 2
fib_last = 1
fib = 1

while len(str(fib)) < 1000:
    fib,fib_last = fib+fib_last,fib
    out += 1

print(out)