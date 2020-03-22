H, W, K = map(int, input().split())

S = [list(map(int, input())) for _ in range(H)]
accS = [[0] * (W + 1) for _ in range(H + 1)]

for h in range(H):
    for w in range(W):
        accS[h + 1][w + 1] = accS[h + 1][w] + accS[h][w + 1] - accS[h][w] + S[h][w]

def isOk(L, left, right):
    for top, bot in zip(L, L[1:]):
        if accS[bot][right] - accS[bot][left] - accS[top][right] + accS[top][left] > K:
            return False
    return True

ans = 10**18

for mask in range(1 << H):
    L = [0] + [d + 1 for d in range(H - 1) if (mask & (1 << d)) > 0] + [H]

    cnt = len(L) - 2
    left = 0
    while left < W:
        right = left
        while right < W and isOk(L, left, right + 1):
            right += 1

        if left == right:
            cnt = 10**18
            break

        cnt += 1
        left = right

    ans = min(ans, cnt - 1)

print(ans)