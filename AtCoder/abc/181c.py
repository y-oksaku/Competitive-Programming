N = int(input())
XY = [tuple(map(int, input().split())) for _ in range(N)]

for i in range(N):
    a, b = XY[i]
    for j in range(i + 1, N):
        x, y = XY[j]
        x -= a
        y -= b
        for k in range(j + 1, N):
            u, v = XY[k]
            u -= a
            v -= b

            u, v = -v, u

            if x * u + y * v == 0:
                print('Yes')
                exit()
print('No')
