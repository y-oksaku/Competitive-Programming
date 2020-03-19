H, W = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(10)]

for k in range(10):
    for i in range(10):
        for j in range(10):
            d = C[i][k] + C[k][j]
            if d < C[i][j]:
                C[i][j] = d

ans = 0
cost = [C[i][1] for i in range(10)]

for _ in range(H):
    for n in map(int, input().split()):
        if n == -1:
            continue
        ans += cost[n]

print(ans)
