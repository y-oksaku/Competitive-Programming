from heapq import heappop, heappush, heapify

N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]
AB.sort(reverse=True)

que = []
ans = 0
for d in range(1, M + 1):
    while AB and AB[-1][0] <= d:
        heappush(que, -AB.pop()[1])
    if que:
        ans += heappop(que)
print(-ans)
