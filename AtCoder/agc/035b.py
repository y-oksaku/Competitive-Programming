N, M = map(int, input().split())

edge = [[] for _ in range(N)]

for _ in range(M) :
    A, B = map(int, input().split())
    edge[A-1].append(B-1)
    edge[B-1].append(A-1)

print(edge)