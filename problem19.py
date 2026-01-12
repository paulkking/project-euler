import datetime

d = datetime.datetime(1901,1,1)
e = datetime.datetime(2001,1,1)

out = 0

while d < e:
    if d.weekday() == 6 and d.day == 1:
        out += 1
    d += datetime.timedelta(days=1)

print(out)