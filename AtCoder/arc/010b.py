from collections import Counter
N = int(input())

holiday = []

dayOfMonth = {
    1 : 31,
    2 : 29,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31
}

month = 1
day = 1

while True:
    holiday.append((month, day))
    day += 7
    if dayOfMonth[month] < day:
        month += 1
        if month >= 13:
            break
        day -= dayOfMonth[month - 1]

month = 1
day = 7

while True:
    holiday.append((month, day))
    day += 7
    if dayOfMonth[month] < day:
        month += 1
        if month >= 13:
            break
        day -= dayOfMonth[month - 1]

for _ in range(N):
    month, day = map(int, input().split('/'))
    holiday.append((month, day))

V = set(holiday)
cntHol = Counter(holiday)

for (month, day), c in cntHol.items():
    if c > 1:
        while True:
            day += 1
            if month < 13 and dayOfMonth[month] < day:
                day = 1
                month += 1
            if (month, day) not in V:
                V.add((month, day))
                break

holiday = list(V)
holiday.sort()

ans = 1
leng = 1
prev = (1, 1)

for month, day in holiday[1:]:
    if month >= 13:
        break
    if day == 1:
        if prev[0] == month - 1 and prev[1] == dayOfMonth[month - 1]:
            leng += 1
        else:
            leng = 1
    else:
        if prev[0] == month and prev[1] == day - 1:
            leng += 1
        else:
            leng = 1
    prev = (month, day)
    ans = max(leng, ans)

print(ans)