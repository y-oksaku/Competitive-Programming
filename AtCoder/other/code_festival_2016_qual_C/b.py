from heapq import heapify, heappop, heappush

K, T = map(int, input().split())
A = [-a for a in map(int, input().split())]

heapify(A)
while len(A) > 1:
    a, b = -heappop(A), -heappop(A)
    heappush(A, -(a - b))

print(max(0, -A[0] - 1))