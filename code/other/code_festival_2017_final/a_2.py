S = input()

T = '*KIH*B*R*'
V = set()

for mask in range(1 << 4):
    cnt = 0
    v = []
    for t in T:
        if t == '*':
            if (mask & (1 << cnt)) != 0:
                v.append('A')
            cnt += 1
        else:
            v.append(t)
    V.add(''.join(v))

if S in V:
    print('YES')
else:
    print('NO')