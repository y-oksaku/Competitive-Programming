H, W = map(int, input().split())
chart = [input() for _ in range(H)]

left = [[0] * W for _ in range(H)]
right = [[0] * W for _ in range(H)]
top = [[0] * W for _ in range(H)]
bottom = [[0] * W for _ in range(H)]

# 左上
for h in range(H):
    for w in range(W):
        if chart[h][w] == '#':
            left[h][w] = 0
            top[h][w] = 0
        else:
            if h >= 1:
                top[h][w] = top[h - 1][w] + 1
            else:
                top[h][w] = 1
            if w >= 1:
                left[h][w] = left[h][w - 1] + 1
            else:
                left[h][w] = 1

for h in range(H)[:: -1]:
    for w in range(W)[:: -1]:
        if chart[h][w] == '#':
            right[h][w] = 0
            bottom[h][w] = 0
        else:
            if h <= H - 2:
                bottom[h][w] = bottom[h + 1][w] + 1
            else:
                bottom[h][w] = 1
            if w <= W - 2:
                right[h][w] = right[h][w + 1] + 1
            else:
                right[h][w] = 1

ans = 1
for h in range(H):
    for w in range(W):
        ans = max(ans, top[h][w] + right[h][w] + bottom[h][w] + left[h][w] - 3)
print(ans)