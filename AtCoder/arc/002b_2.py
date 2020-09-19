y, m, d = map(int, input().split('/'))

date = {
    1: 31,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

def feb(y):
    if y % 4 != 0:
        return 28
    if y % 400 == 0:
        return 29
    if y % 100 == 0:
        return 28
    return 29

while True:
    if y % (m * d) == 0:
        print(f'{y:04}/{m:02}/{d:02}')
        break
    d += 1
    M = date[m] if m != 2 else feb(y)

    if d > M:
        m += 1
        d = 1
    if m > 12:
        y += 1
        m = 1
