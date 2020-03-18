import sys
input = sys.stdin.buffer.readline

N, K = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(K)]

edges = [[] for _ in range(N)]

def sol(s, t):
    minDist = [10**10] * N
    minDist[s] = 0
    confilm = [False] * N

    for _ in range(N):
        now = None
        mi = 10**10
        for i in range(N):
            if confilm[i]:
                continue
            if mi > minDist[i]:
                now = i
                mi = minDist[i]

        if now == None:
            break

        confilm[now] = True

        for to, cost in edges[now]:
            d = mi + cost
            if d < minDist[to]:
                minDist[to] = d

    return minDist[t] if minDist[t] < 10**10 else -1

ans = []
for L in A:
    if L[0] == 0:
        ans.append(sol(L[1] - 1, L[2] - 1))
    else:
        edges[L[1] - 1].append((L[2] - 1, L[3]))
        edges[L[2] - 1].append((L[1] - 1, L[3]))

print(*ans, sep='\n')
