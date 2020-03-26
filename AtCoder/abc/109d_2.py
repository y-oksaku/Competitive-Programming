H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

cnt = 0
ans = []
for h in range(H - 1):
    for w in range(W):
        if A[h][w] % 2 == 1:
            cnt += 1
            ans.append((h, w, h + 1, w))
            A[h + 1][w] += 1
            A[h][w] -= 1

for w in range(W - 1):
    if A[H - 1][w] % 2 == 1:
        cnt += 1
        ans.append((H - 1, w, H - 1, w + 1))
        A[H - 1][w + 1] += 1
        A[H - 1][w] -= 1

print(cnt)
for a, b, c, d in ans:
    print(a + 1, b + 1, c + 1, d + 1)
