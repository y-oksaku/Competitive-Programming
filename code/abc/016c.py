N, M = map(int, input().split())

edge = [set([]) for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].add(b)
    edge[b].add(a)

for i in range(N):
    A = set([])
    for friend in edge[i]:
        for a in edge[friend]:
            if a == i or a in edge[i]:
                continue
            A.add(a)
    print(len(A))