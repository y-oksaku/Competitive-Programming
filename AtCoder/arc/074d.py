from heapq import heappush, heappop, heapify

N = int(input())
A = list(map(int, input().split()))
B = [-a for a in A[:: -1]]

L = [0] * (N * 3)
que = A[:N]
heapify(que)
now = sum(A[:N])
for mid in range(N, N * 2 + 1):
    L[mid] = now
    a = A[mid]
    if a > que[0]:
        now -= heappop(que)
        heappush(que, a)
        now += a

R = [0] * (N * 3)
que = B[:N]
heapify(que)
now = sum(B[:N])
for mid in range(N, N * 2 + 1):
    R[mid] = now
    a = B[mid]
    if a > que[0]:
        now -= heappop(que)
        heappush(que, a)
        now += a

R = R[:: -1]

ans = -10**18
for mid in range(N, N * 2 + 1):
    x = L[mid] + R[mid - 1]
    ans = max(ans, x)

print(ans)