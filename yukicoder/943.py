N = int(input())
INF = 10**10

parent = []
for _ in range(N):
    state = 0
    for i, s in enumerate(input().split()):
        if s == '1':
            state |= (1 << i)
    parent.append(state)
A = tuple(map(int, input().split()))

ans = INF
for mask in range(1 << N):
    state = mask
    V = set(range(N))

    while True:
        W = set()
        for v in V:
            if (parent[v] & state) == parent[v]:
                state |= (1 << v)
            else:
                W.add(v)
        if W == V:
            break
        V = W
        if len(V) == 0:
            cost = 0
            for i, a in enumerate(A):
                if (mask & (1 << i)) != 0:
                    cost += a
            ans = min(ans, cost)
            break

print(ans)
