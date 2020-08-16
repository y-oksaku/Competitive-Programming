N, K = map(int, input().split())
P = list(map(lambda a: int(a) - 1, input().split()))
C = list(map(int, input().split()))
INF = 10**18

grp = []
visited = [False] * N

for i in range(N):
    if visited[i]:
        continue
    V = []
    while not visited[i]:
        V.append(i)
        visited[i] = True
        i = P[i]
    grp.append(V)

def solve(V, K):
    N = len(V)
    sumC = 0
    for v in V:
        sumC += C[v]

    ans = 0
    if sumC > 0 and K >= N:
        q, K = divmod(K, N)
        K += N
        ans = sumC * (q - 1)
    else:
        K = min(K, N)

    if K == 0:
        return ans

    def calc(now):
        acc = C[now]
        ret = acc
        for _ in range(K - 1):
            now = P[now]
            acc += C[now]
            ret = max(ret, acc)
        return ret

    mx = -INF
    for start in V:
        mx = max(mx, calc(start))

    return mx + ans

ans = max(C)
for V in grp:
    ans = max(ans, solve(V, K))
print(ans)


