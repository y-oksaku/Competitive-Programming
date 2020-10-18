H, W = map(int, input().split())
S = [input() for _ in range(H)]

ans = 0
for h in range(H):
    for w in range(W - 1):
        if S[h][w] == S[h][w + 1] == '.':
            ans += 1
for h in range(H - 1):
    for w in range(W):
        if S[h][w] == S[h + 1][w] == '.':
            ans += 1
print(ans)
