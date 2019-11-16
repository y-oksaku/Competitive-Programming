from heapq import heappop, heappush, heapify

N, M = map(int, input().split())
A = list(map(int, input().split()))
A = [-a for a in A]
heapify(A)

for _ in range(M):
    top = heappop(A)
    top *= -1
    top //= 2
    heappush(A, -top)

print(-sum(A))