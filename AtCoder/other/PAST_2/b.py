N, M, Q = map(int, input().split())

ans = [[] for _ in range(N + 1)]
points = [N] * (M + 1)

for _ in range(Q):
    query = tuple(map(int, input().split()))

    if query[0] == 1:
        s = 0
        for m in ans[query[1]]:
            s += points[m]
        print(s)
    else:
        n, m = query[1:]
        ans[n].append(m)
        points[m] -= 1
