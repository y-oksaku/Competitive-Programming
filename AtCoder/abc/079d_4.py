H, W = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(10)]
A = [list(map(int, input().split())) for _ in range(H)]

for k in range(10):
    for i in range(10):
        for j in range(10):
            d = C[i][k] + C[k][j]
            if C[i][j] > d:
                C[i][j] = d

cost = [C[d][1] for d in range(10)]

ans = 0
for R in A:
    for a in R:
        if a == -1:
            continue
        ans += cost[a]
print(ans)
