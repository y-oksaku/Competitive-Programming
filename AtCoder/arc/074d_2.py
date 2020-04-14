from heapq import heappush, heappop, heapify
N = int(input())
M = 3 * N
A = list(map(int, input().split()))
B = A[::-1]

L = [0] * (N + 1)
que = A[:N]
heapify(que)
S = sum(que)
L[0] = S
for i, a in enumerate(A[N: 2 * N], start=1):
    S += a
    heappush(que, a)
    S -= heappop(que)
    L[i] = S

R = [0] * (N + 1)
que = [-a for a in B[:N]]
heapify(que)
S = sum(que)
R[0] = S
for i, b in enumerate(B[N: 2 * N], start=1):
    b = -b
    S += b
    heappush(que, b)
    S -= heappop(que)
    R[i] = S
R = R[::-1]

ans = -10**18
for l, r in zip(L, R):
    ans = max(ans, l + r)
print(ans)
