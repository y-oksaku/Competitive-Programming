S, T = input().split()
N = int(input())

W = set([input() for _ in range(N)])
W.add(S)
W.add(T)
W = list(W)

WtoI = {w: i for i, w in enumerate(W)}

def canGo(A, B):
    cnt = 0
    for a, b in zip(A, B):
        if a != b:
            cnt += 1
        if cnt > 1:
            return False
    return cnt == 1

edges = []
for fr in W:
    for to in W:
        i = WtoI[fr]
        j = WtoI[to]

        if canGo(fr, to):
            edges.append((i, j))

M = len(W)
INF = 10**18
minDist = [INF] * M
minDist[WtoI[S]] = 0
prev = [None] * M
for _ in range(N):
    for fr, to in edges:
        d = minDist[fr] + 1
        if minDist[to] > d:
            minDist[to] = d
            prev[to] = fr

if minDist[WtoI[T]] == INF:
    print(-1)
    exit()

now = WtoI[T]
ans = [now]
while now != WtoI[S]:
    now = prev[now]
    ans.append(now)
ans = ans[::-1]

ans = [W[i] for i in ans]

if len(ans) == 1:
    ans += ans

print(len(ans) - 2)
print(*ans, sep='\n')
