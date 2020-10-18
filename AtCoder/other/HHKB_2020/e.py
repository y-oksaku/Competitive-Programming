H, W = map(int, input().split())
S = [input() for _ in range(H)]
MOD = 10**9 + 7
K = sum(s.count('.') for s in S)

cnt = [[0] * W for _ in range(H)]

for h in range(H):
    l = 0
    for w in range(W):
        cnt[h][w] += l
        if S[h][w] == '.':
            l += 1
        else:
            l = 0
    r = 0
    for w in range(W)[::-1]:
        cnt[h][w] += r
        if S[h][w] == '.':
            r += 1
        else:
            r = 0
for w in range(W):
    t = 0
    for h in range(H):
        cnt[h][w] += t
        if S[h][w] == '.':
            t += 1
        else:
            t = 0
    b = 0
    for h in range(H)[::-1]:
        cnt[h][w] += b
        if S[h][w] == '.':
            b += 1
        else:
            b = 0

ans = K * pow(2, K, MOD)
for h in range(H):
    for w in range(W):
        if S[h][w] == '#':
            continue
        c = cnt[h][w] + 1
        ans -= pow(2, K - c, MOD)
        ans %= MOD
print(ans)
