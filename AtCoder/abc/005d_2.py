N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]

accD = [[0] * (N + 1) for _ in range(N + 1)]
for h in range(1, N + 1):
    for w in range(1, N + 1):
        accD[h][w] = accD[h - 1][w] + accD[h][w - 1] - accD[h - 1][w - 1] + D[h - 1][w - 1]

ans = [0] * (N**2 + 1)
for top in range(N):
    for left in range(N):
        for bottom in range(top, N + 1):
            for right in range(left, N + 1):
                size = (right - left) * (bottom - top)
                area = accD[bottom][right] - accD[top][right] - accD[bottom][left] + accD[top][left]
                ans[size] = max(ans[size], area)

for i in range(1, N**2 + 1):
    ans[i] = max(ans[i], ans[i - 1])

Q = int(input())
for _ in range(Q):
    P = int(input())
    print(ans[P])
