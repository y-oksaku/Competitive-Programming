x, y, W = input().split()
x = int(x) - 1
y = int(y) - 1

chart = [input() for _ in range(9)]

ans = ''

for _ in range(4):
    ans += chart[y][x]

    if W == 'R':
        if x == 8:
            x = 7
            W = 'L'
        else:
            x += 1
    elif W == 'L':
        if x == 0:
            x = 1
            W = 'R'
        else:
            x -= 1
    elif W == 'U':
        if y == 0:
            y = 1
            W = 'D'
        else:
            y -= 1
    elif W == 'D':
        if y == 8:
            y = 7
            W = 'U'
        else:
            y += 1
    elif W == 'RU':
        if x == 8 and y == 0:
            x = 7
            y = 1
            W = 'LD'
        elif x == 8:
            x = 7
            y -= 1
            W = 'LU'
        elif y == 0:
            x += 1
            y = 1
            W = 'RD'
        else:
            x += 1
            y -= 1
    elif W == 'RD':
        if x == 8 and y == 8:
            x = 7
            y = 7
            W = 'LU'
        elif x == 8:
            x = 7
            y += 1
            W = 'LD'
        elif y == 8:
            x += 1
            y = 7
            W = 'RU'
        else:
            x += 1
            y += 1
    elif W == 'LU':
        if x == 0 and y == 0:
            x = 1
            y = 1
            W = 'RD'
        elif x == 0:
            x = 1
            y -= 1
            W = 'RU'
        elif y == 0:
            x -= 1
            y = 1
            W = 'LD'
        else:
            x -= 1
            y -= 1
    elif W == 'LD':
        if x == 0 and y == 8:
            x = 1
            y = 7
            W = 'RU'
        elif x == 0:
            x = 1
            y += 1
            W = 'RD'
        elif y == 8:
            x -= 1
            y = 7
            W = 'LU'
        else:
            x -= 1
            y += 1

print(ans)