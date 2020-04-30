H, W = map(int, input().split())
A = [input() for _ in range(H)]

U = [[0] * W for _ in range(H)]
L = [[0] * W for _ in range(H)]
D = [[0] * W for _ in range(H)]
R = [[0] * W for _ in range(H)]

for h in range(H):
    for w in range(W):
        if A[h][w] == '#':
            U[h][w] = 0
            L[h][w] = 0
        else:
            U[h][w] = 1 + (U[h - 1][w] if h > 0 else 0)
            L[h][w] = 1 + (L[h][w - 1] if w > 0 else 0)

        y = H - h - 1
        x = W - w - 1
        if A[y][x] == '#':
            D[y][x] = 0
            R[y][x] = 0
        else:
            D[y][x] = 1 + (D[y + 1][x] if y < H - 1 else 0)
            R[y][x] = 1 + (R[y][x + 1] if x < W - 1 else 0)

ans = 0
for h in range(H):
    for w in range(W):
        if A[h][w] == '.':
            ans = max(ans, U[h][w] + D[h][w] + L[h][w] + R[h][w] - 3)
print(ans)
