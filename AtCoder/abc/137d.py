import heapq

N, M = map(int, input().split())
arb = [[] for _ in range(M + 1)]

for _ in range(N) :
    a, b = map(int, input().split())
    if a <= M :
        arb[a].append(-b)

arbList = []

ans = 0
for day in range(M + 1) :
    for b in arb[day] :
        heapq.heappush(arbList, b)
    if arbList :
        ans += heapq.heappop(arbList)

print(-ans)