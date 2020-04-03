H, W = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(10)]

for k in range(10):
    for i in range(10):
        for j in range(10):
            d = C[i][k] + C[k][j]
            if C[i][j] > d:
                C[i][j] = d

cost = [C[j][1] for j in range(10)]
ans = 0

for _ in range(H):
    for n in map(int, input().split()):
        if n == -1:
            continue
        ans += cost[n]
print(ans)