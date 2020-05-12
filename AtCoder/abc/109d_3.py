H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

ans = []
for h in range(H - 1):
    for w in range(W):
        if A[h][w] % 2 == 1:
            A[h][w] -= 1
            A[h + 1][w] += 1
            ans.append((h + 1, w + 1, h + 2, w + 1))
for w in range(W - 1):
    if A[H - 1][w] % 2 == 1:
        A[H - 1][w] -= 1
        A[H - 1][w + 1] += 1
        ans.append((H, w + 1, H, w + 2))

print(len(ans))
for a in ans:
    print(*a)
