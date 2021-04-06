from collections import deque
from string import ascii_lowercase as alph

from collections import deque

H, W = map(int, input().split())
A = [input() for _ in range(H)]
INF = 10**18

alphList = {s: deque() for s in alph}
sh, sw = -1, -1
gh, gw = -1, -1

for h, S in enumerate(A):
    for w, s in enumerate(S):
        if s == 'S':
            sh, sw = h, w
        if s == 'G':
            gh, gw = h, w
        if 'a' <= s <= 'z':
            alphList[s].append((h, w))

minDist = [[INF] * W for _ in range(H)]
minDist[sh][sw] = 0

que = deque([(sh, sw)])
while que:
    h, w = que.popleft()
    now = minDist[h][w]

    for dh, dw in ((h + 1, w), (h - 1, w), (h, w + 1), (h, w - 1)):
        if 0 <= dh < H and 0 <= dw < W and minDist[dh][dw] == INF and A[h][w] != '#':
            minDist[dh][dw] = now + 1
            que.append((dh, dw))
    if 'a' <= A[h][w] <= 'z':
        while alphList[A[h][w]]:
            dh, dw = alphList[A[h][w]].pop()
            if minDist[dh][dw] == INF:
                minDist[dh][dw] = now + 1
                que.append((dh, dw))

ans = minDist[gh][gw]
print(ans if ans < INF else -1)
