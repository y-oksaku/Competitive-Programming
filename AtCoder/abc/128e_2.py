import sys
input = sys.stdin.readline
from collections import defaultdict
from heapq import heappop, heappush

N, Q = map(int, input().split())
INF = float('inf')

events = []
for i in range(N):
    S, T, X = map(int, input().split())
    events.append((S - X, 0, X))
    events.append((T - X, 1, X))

for _ in range(Q):
    events.append((int(input()), 2, 0))

events.sort()

cnt = defaultdict(int)
cnt[INF] += 1
que = [INF]

for t, flag, x in events:
    if flag == 0:
        if cnt[x] == 0:
            heappush(que, x)
        cnt[x] += 1
    elif flag == 1:
        cnt[x] -= 1
    else:
        while cnt[que[0]] == 0:
            heappop(que)
        print(que[0] if que[0] != INF else -1)

