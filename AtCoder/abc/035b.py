S = input()
T = input()

x, y = 0, 0
cnt = 0
for s in S:
    if s == 'L':
        x -= 1
    elif s == 'R':
        x += 1
    elif s == 'U':
        y += 1
    elif s == 'D':
        y -= 1
    else:
        cnt += 1

if T == '1':
    print(abs(x) + abs(y) + cnt)
else:
    if abs(x) + abs(y) >= cnt:
        print(abs(x) + abs(y) - cnt)
    else:
        print((cnt - abs(x) - abs(y)) % 2)

