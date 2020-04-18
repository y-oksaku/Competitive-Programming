N, Q = map(int, input().split())
query = [tuple(map(int, input().split())) for _ in range(Q)]

S = [set() for _ in range(N + 1)]
for q in query:
    if q[0] == 1:
        _, a, b = q
        S[a].add(b)
    if q[0] == 2:
        a = q[1]
        for i in range(1, N + 1):
            if a in S[i]:
                S[a].add(i)
    if q[0] == 3:
        a = q[1]
        V = set([a])
        for to in S[a]:
            V |= S[to]
        V.remove(a)
        S[a] |= V

ans = []
for i in range(1, N + 1):
    a = ''.join(['Y' if i != j and j in S[i] else 'N' for j in range(1, N + 1)])
    ans.append(a)

print(*ans, sep='\n')
