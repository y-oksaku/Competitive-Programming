from collections import deque

H, W, K = map(int, input().split())

chart = [list(input()) for _ in range(H)]

start = (-1, -1)
for h in range(H):
    for w in range(W):
        if chart[h][w] == 'S':
            start = (h, w)
            chart[h][w] = '.'

minDist  = [[float('inf')] * W for _ in range(H)]
que = deque([(start[0], start[1], 0)])
while que:
    nh, nw, dist = que.popleft()

    if minDist[nh][nw] <= dist:
        continue

    minDist[nh][nw] = dist
    if dist == K:
        continue

    for toH in [nh - 1, nh + 1]:
        if toH < 0 or toH >= H:
            continue
        if chart[toH][nw] == '.':
            que.append((toH, nw, dist + 1))
    for toW in [nw - 1, nw + 1]:
        if toW < 0 or toW >= W:
            continue
        if chart[nh][toW] == '.':
            que.append((nh, toW, dist + 1))

ans = float('inf')
for h in range(H):
    for w in range(W):
        if minDist[h][w] == float('inf'):
            continue
        d = min(h, w, H - h - 1, W - w - 1)
        if d == 0:
            ans = min(ans, 1)
        else:
            ans = min(ans, -(-d // K) + 1)

print(ans)