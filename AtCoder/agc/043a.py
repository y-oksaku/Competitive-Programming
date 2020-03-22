from collections import deque
from functools import lru_cache

H, W = map(int, input().split())
S = [input() for _ in range(H)]

minDist = [[10**10] * W for _ in range(H)]
que = deque([(0, 0, 0 if S[0][0] == '.' else 1, S[0][0] == '.')])

while que:
    h, w, dist, isWhite = que.popleft()

    if minDist[h][w] <= dist:
        continue
    minDist[h][w] = dist

    if h + 1 < H:
        isNextWhite = S[h + 1][w] == '.'
        if isWhite and not isNextWhite:
            que.append((h + 1, w, dist + 1, isNextWhite))
        else:
            que.appendleft((h + 1, w, dist, isNextWhite))
    if w + 1 < W:
        isNextWhite = S[h][w + 1] == '.'
        if isWhite and not isNextWhite:
            que.append((h, w + 1, dist + 1, isNextWhite))
        else:
            que.appendleft((h, w + 1, dist, isNextWhite))

ans = minDist[H - 1][W - 1]
print(ans)
