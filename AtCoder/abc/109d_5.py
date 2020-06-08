H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

ans = []
for h in range(H - 1):
    for w in range(W):
        if A[h][w] % 2 == 1:
            A[h][w] -= 1
            A[h + 1][w] += 1
            ans.append((h, w, h + 1, w))

for w in range(W - 1):
    if A[H - 1][w] % 2 == 1:
        A[H - 1][w] -= 1
        A[H - 1][w + 1] += 1
        ans.append((H - 1, w, H - 1, w + 1))

print(len(ans))
for h, w, x, y in ans:
    print(h + 1, w + 1, x + 1, y + 1)
