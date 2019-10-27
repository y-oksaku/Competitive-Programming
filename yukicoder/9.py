from heapq import heapify, heappop, heappush

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

myMonster = [(a, 0) for a in A]
heapify(myMonster)
ans = float('inf')

for start in range(N):
    A = myMonster[:]
    for b in B[start:] + B[:start]:
        now, time = heappop(A)
        now += b // 2
        heappush(A, (now, time + 1))
    ans = min(ans, max([a for _, a in A]))

print(ans)