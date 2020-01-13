H, W = map(int, input().split())
N = H * W

chart = [input() for _ in range(H)]

def node(h, w):
    return h * W + w

minDist = [[10**10] * N for _ in range(N)]

for i in range(N):
    minDist[i][i] = 0

for h in range(H):
    for w in range(W):
        if chart[h][w] == '#':
            continue

        if h > 0 and chart[h - 1][w] == '.':
            minDist[node(h, w)][node(h - 1, w)] = 1
            minDist[node(h - 1, w)][node(h, w)] = 1
        if h < H - 1 and chart[h + 1][w] == '.':
            minDist[node(h, w)][node(h + 1, w)] = 1
            minDist[node(h + 1, w)][node(h, w)] = 1
        if w > 0 and chart[h][w - 1] == '.':
            minDist[node(h, w)][node(h, w - 1)] = 1
            minDist[node(h, w - 1)][node(h, w)] = 1
        if w < W - 1 and chart[h][w + 1] == '.':
            minDist[node(h, w)][node(h, w + 1)] = 1
            minDist[node(h, w + 1)][node(h, w)] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            d = minDist[i][k] + minDist[k][j]
            if minDist[i][j] > d:
                minDist[i][j] = d

ans = 0
for dists in minDist:
    for d in dists:
        if d < 10**10:
            ans = max(ans, d)

print(ans)