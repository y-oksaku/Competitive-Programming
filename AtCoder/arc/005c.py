import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7
INF = float('inf')

def sol():
    H, W = map(int, input().split())
    chart = [input().rstrip() for _ in range(H)]

    start = (0, 0)
    end = (0, 0)
    for h in range(H):
        for w in range(W):
            if chart[h][w] == 's':
                start = (h, w)
            if chart[h][w] == 'g':
                end = (h, w)

    que = deque([(start, 0)])
    visited = [[False] * W for _ in range(H)]
    while que:
        (h, w), dist = que.popleft()

        if visited[h][w]:
            continue

        visited[h][w] = True

        if (h, w) == end:
            if dist <= 2:
                print('YES')
            else:
                print('NO')
            break

        if h > 0 and visited[h - 1][w] == False:
            if chart[h - 1][w] != '#':
                que.appendleft(((h - 1, w), dist))
            else:
                que.append(((h - 1, w), dist + 1))
        if h < H - 1 and visited[h + 1][w] == False:
            if chart[h + 1][w] != '#':
                que.appendleft(((h + 1, w), dist))
            else:
                que.append(((h + 1, w), dist + 1))
        if w > 0 and visited[h][w - 1] == False:
            if chart[h][w - 1] != '#':
                que.appendleft(((h, w - 1), dist))
            else:
                que.append(((h, w - 1), dist + 1))
        if w < W - 1 and visited[h][w + 1] == False:
            if chart[h][w + 1] != '#':
                que.appendleft(((h, w + 1), dist))
            else:
                que.append(((h, w + 1), dist + 1))

sol()