H, W = map(int, input().split())

black = [[0] * W for _ in range(H)]
white = [[0] * W for _ in range(H)]

for h in range(H):
    for w, c in enumerate(map(int, input().split())):
        if (h + w) % 2 == 0:
            black[h][w] = c
        else:
            white[h][w] = c

blackSum = [[0] * (W + 1) for _ in range(H + 1)]
whiteSum = [[0] * (W + 1) for _ in range(H + 1)]

for h in range(1, H + 1):
    for w in range(1, W + 1):
        blackSum[h][w] = blackSum[h - 1][w] + blackSum[h][w - 1] - blackSum[h - 1][w - 1] + black[h - 1][w - 1]
        whiteSum[h][w] = whiteSum[h - 1][w] + whiteSum[h][w - 1] - whiteSum[h - 1][w - 1] + white[h - 1][w - 1]

ans = 0
for top in range(H):
    for left in range(W):
        for bottom in range(top + 1, H + 1):
            for right in range(left + 1, W + 1):
                blackC = blackSum[bottom][right] - blackSum[bottom][left] - blackSum[top][right] + blackSum[top][left]
                whiteC = whiteSum[bottom][right] - whiteSum[bottom][left] - whiteSum[top][right] + whiteSum[top][left]
                if blackC == whiteC:
                    ans = max(ans, (bottom - top) * (right - left))

print(ans)