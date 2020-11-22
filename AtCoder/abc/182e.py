H, W, N, M = map(int, input().split())
S = [[0] * (W + 2) for _ in range(H + 2)]

for h in range(H + 2):
    S[h][0] = -1
    S[h][W + 1] = -1
for w in range(W + 2):
    S[0][w] = -1
    S[H + 1][w] = -1

AB = [tuple(map(int, input().split())) for _ in range(N)]

for _ in range(M):
    c, d = map(int, input().split())
    S[c][d] = -1

def search(dh, dw):
    visited = [[0] * (W + 2) for _ in range(H + 2)]

    for a, b in AB:
        while not visited[a][b] and S[a][b] != -1:
            S[a][b] = 1
            visited[a][b] = True
            a += dh
            b += dw

search(0, 1)
search(0, -1)
search(1, 0)
search(-1, 0)

ans = 0
for line in S:
    ans += line.count(1)
print(ans)
