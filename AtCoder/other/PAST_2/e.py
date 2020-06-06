N, M, Q = map(int, input().split())

edges = [[] for _ in range(N + 1)]
for _ in range(M):
    fr, to = map(int, input().split())
    edges[fr].append(to)
    edges[to].append(fr)

C = [-1] + list(map(int, input().split()))

for _ in range(Q):
    q, *A = map(int, input().split())

    if q == 1:
        c = C[A[0]]
        print(c)
        for to in edges[A[0]]:
            C[to] = c
    else:
        x, y = A
        print(C[x])
        C[x] = y
