N, K = map(int, input().split())
B = [[-1] * N for _ in range(K)]

ans = [[] for _ in range(N)]
V = set()
for n in range(N):
    for k, id in enumerate(map(int, input().split())):
        B[k][n] = id

    W = set()
    L = K
    for k in range(K):
        for i in range(N):
            L -= 1
            if L < 0:
                break
            id = B[k][i]
            if id == -1:
                continue
            if id in W:
                L += 1
                continue
            if id in V:
                W.add(id)
                continue
            ans[n].append(id)
            W.add(id)
    V |= W

for a in ans:
    a.sort()
    print(*a)
