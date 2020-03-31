N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

ans = [[] for _ in range(N)]
order = [[0] * N for _ in range(K)]
appended = set([0])

for n, line in enumerate(A):
    for rank, id in enumerate(line):
        order[rank][n] = id

    cnt = 0
    R = K
    V = set()
    for rank in range(K):
        for id in order[rank]:
            cnt += 1
            if not id in appended:
                ans[n].append(id)
                appended.add(id)
            elif id in V and id != 0:
                R += 1
            V.add(id)
            if cnt >= R:
                break
        if cnt >= R:
            break

for rank in range(K):
    for id in order[rank]:
        if not id in appended and len(appended) <= K:
            ans[-1].append(id)
            appended.add(id)

for a in ans:
    a.sort()
    print(*a)
