N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]
XY = [tuple(map(int, input().split())) for _ in range(M)]

ans = [0] * N
for i, (a, b) in enumerate(AB):
    d = abs(XY[0][0] - a) + abs(XY[0][1] - b)
    for j, (x, y) in enumerate(XY):
        e = abs(a - x) + abs(b - y)
        if d > e:
            ans[i] = j
            d = e

print(*[a + 1 for a in ans], sep='\n')
