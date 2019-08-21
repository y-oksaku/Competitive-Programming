from collections import deque
H, W, T = map(int, input().split())
M = [0] * H
INF = float('inf')

start = (0, 0)
goal = (0, 0)

for i in range(H):
    M[i] = input()
    for j in range(W):
        if M[i][j] == 'S':
            start = (i, j)
        elif M[i][j] == 'G':
            goal = (i, j)

def minDist(cost):
    dist = [[INF for _ in range(W)] for _ in range(H)]
    dist[start[0]][start[1]] = 0

    que = deque([])
    que.append(start)

    while que:
        h, w = que.popleft()

        if h > 0:
            c = cost if M[h - 1][w] == '#' else 1
            if dist[h][w] + c < dist[h - 1][w]:
                dist[h - 1][w] = dist[h][w] + c
                que.append((h - 1, w))
        if h < H - 1:
            c = cost if M[h + 1][w] == '#' else 1
            if dist[h][w] + c < dist[h + 1][w]:
                dist[h + 1][w] = dist[h][w] + c
                que.append((h + 1, w))
        if w > 0:
            c = cost if M[h][w - 1] == '#' else 1
            if dist[h][w] + c < dist[h][w - 1]:
                dist[h][w - 1] = dist[h][w] + c
                que.append((h, w - 1))
        if w < W - 1:
            c = cost if M[h][w + 1] == '#' else 1
            if dist[h][w] + c < dist[h][w + 1]:
                dist[h][w + 1] = dist[h][w] + c
                que.append((h, w + 1))

    return dist[goal[0]][goal[1]]

maxLeng = minDist(1000)
blackCount = maxLeng // 1000
whiteCount = maxLeng % 1000

bigAns = (T - whiteCount) // blackCount

left = 1
right = H * W + 1

while right - left > 1:
    mid = (left + right) // 2
    if minDist(mid) <= T:
        left = mid
    else:
        right = mid

ans = max(bigAns, left)
print(ans)