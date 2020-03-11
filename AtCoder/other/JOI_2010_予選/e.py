from collections import deque
import sys
input = sys.stdin.readline

H, W, N = map(int, input().split())
A = [input().strip() for _ in range(H)]
P = [None] * (N + 1)

for h in range(H):
    for w in range(W):
        s = A[h][w]
        if s == '.' or s == 'X':
            continue
        if s == 'S':
            P[0] = (h, w)
        else:
            P[int(s)] = (h, w)

def bfs(fr, to):
    sh, sw = fr
    que = deque([(sh, sw, 0)])
    dist = [[10**10] * W for _ in range(H)]

    while que:
        h, w, d = que.popleft()

        if dist[h][w] <= d:
            continue
        if (h, w) == to:
            return d
        dist[h][w] = d

        for dh, dw in zip([0, 0, 1, -1], [1, -1, 0, 0]):
            toH, toW = h + dh, w + dw
            if 0 <= toH < H and 0 <= toW < W and A[toH][toW] != 'X':
                que.append((toH, toW, d + 1))
    return 10**10

ans = 0
for fr, to in zip(P, P[1:]):
    ans += bfs(fr, to)

print(ans)
