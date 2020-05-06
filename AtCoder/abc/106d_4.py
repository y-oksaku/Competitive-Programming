N, M, Q = map(int, input().split())

A = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    L, R = map(int, input().split())
    A[L][R] += 1

for i in range(1, N + 1):
    for j in range(1, N + 1):
        A[i][j] += A[i][j - 1]
for j in range(1, N + 1):
    for i in range(1, N + 1):
        A[i][j] += A[i - 1][j]

ans = []
for _ in range(Q):
    p, q = map(int, input().split())
    p -= 1
    ans.append(A[q][q] - A[q][p] - A[p][q] + A[p][p])
print(*ans, sep='\n')
