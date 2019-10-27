diff = 1000
total = 0

for i in range(5) :
    time = int(input())
    if time % 10 > 0 :
        diff = min(diff,time % 10)
    total += int((time + 9) / 10) * 10

if diff == 1000 :
    print(total)
else :
    print(total - 10 + diff)