N, D = map(int, input().split())
L = [i * i for i in range(1, N + 1)]

YZ = [0] * (2 * (N**2) + 1)
for i in L:
    for j in L:
        YZ[i + j] += 1

XW = [0] * (2 * (N**2) + 1 + D)
for w in L:
    for x in L:
        if D + w - x < 0:
            break
        XW[D + w - x] += 1

ans = 0
for i in range(2 * (N**2) + 1):
    ans += YZ[i] * XW[i]
print(ans)