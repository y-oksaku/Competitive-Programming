from collections import deque

H, W = map(int, input().split())
A = [input() for _ in range(H)]

minDist = [[10**10] * W for _ in range(H)]
que = deque([])
for h in range(H):
    for w in range(W):
        if A[h][w] == '#':
            que.append((h, w, 0))
            minDist[h][w] = 0

while que:
    h, w, d = que.popleft()

    if minDist[h][w] < d:
        continue
    minDist[h][w] = d

    for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if 0 <= dh + h < H and 0 <= dw + w < W:
            if minDist[dh + h][dw + w] > d + 1:
                que.append((dh + h, dw + w, d + 1))
                minDist[dh + h][dw + w] = d + 1

ans = max(max(d) for d in minDist)
print(ans)
