from collections import deque

X, Y, A, B, C = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
R = list(map(int, input().split()))

R.sort()
R = deque(R)

P.sort(reverse=True)
Q.sort(reverse=True)
P = P[:X]
Q = Q[:Y]

S = [P, Q]

A = [(0, i, p) for i, p in enumerate(P)] + [(1, i, q) for i, q in enumerate(Q)]
A.sort(reverse=True, key=lambda a: a[2])

while R and R[-1] > A[-1][2]:
    k, i, _ = A.pop()
    S[k][i] = R.pop()

print(sum(P) + sum(Q))
