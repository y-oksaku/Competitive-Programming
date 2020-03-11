from collections import deque

H, W = map(int, input().split())
A = [input() for _ in range(H)]

que = deque([(0, 0, 1)])
minDist = [[10**10] * W for _ in range(H)]

while que:
    h, w, d = que.popleft()

    if minDist[h][w] <= d:
        continue
    minDist[h][w] = d

    if (h, w) == (H - 1, W - 1):
        break

    for dh, dw in zip([0, 0, 1, -1], [1, -1, 0, 0]):
        toH, toW = h + dh, w + dw
        if 0 <= toH < H and 0 <= toW < W and A[toH][toW] == '.':
            que.append((toH, toW, d + 1))

if minDist[H - 1][W - 1] == 10**10:
    print(-1)
    exit()

white = sum([a.count('.') for a in A])
print(max(0, white - minDist[H - 1][W - 1]))
