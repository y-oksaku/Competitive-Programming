from heapq import heappush, heappop
import sys
input = sys.stdin.buffer.readline

N, Q = map(int, input().split())
E = []

for i in range(N):
    s, t, x = map(int, input().split())
    E.append((0, t - x, x, i))
    E.append((1, s - x, x, i))

D = [int(input()) for _ in range(Q)]

E.sort(key=lambda a: a[1], reverse=True)

ans = []
que = [(10**18, -1)]
V = set()
for d in D:
    while E and E[-1][1] <= d:
        f, _, x, i = E.pop()
        if f == 0:
            V.add(i)
        else:
            heappush(que, (x, i))
    while que[0][1] in V:
        heappop(que)
    ans.append(que[0][0])

ans = [a if a < 10**18 else -1 for a in ans]
print(*ans, sep='\n')
