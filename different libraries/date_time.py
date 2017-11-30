import datetime

n = input().split()
add_day = int(input())

date = datetime.date(int(n[0]), int(n[1]), int(n[2]))
delta = datetime.timedelta(days=add_day)
res = date + delta
print(res.strftime('%Y %m %d'))

