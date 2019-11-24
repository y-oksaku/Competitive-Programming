H, W, K, V = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(H)]

cumA = [[0] * (W + 1) for _ in range(H + 1)]

for h in range(1, H + 1):
    for w in range(1, W + 1):
        cumA[h][w] = cumA[h - 1][w] + cumA[h][w - 1] - cumA[h - 1][w - 1] + A[h - 1][w - 1]

ans = 0
for t in range(H + 1):
    for b in range(t + 1, H + 1):
        for l in range(W + 1):
            for r in range(l + 1, W + 1):
                cnt = (b - t) * (r - l)
                area = cumA[b][r] - cumA[b][l] - cumA[t][r] + cumA[t][l]
                if cnt * K + area <= V:
                    ans = max(ans, cnt)

print(ans)