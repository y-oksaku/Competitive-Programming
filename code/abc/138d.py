import sys
sys.setrecursionlimit(10**7)

def sol():
    N, Q = map(int, input().split())
    edge = [[] for _ in range(N)]

    for _ in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edge[a].append(b)
        edge[b].append(a)

    ans = [0 for _ in range(N)]

    for _ in range(Q):
        p, x = map(int, input().split())
        p -= 1
        ans[p] += x

    def calc(now, parent):
        if parent != -1:
            ans[now] += ans[parent]
        for to in edge[now]:
            if to != parent:
                calc(to, now)
        return

    calc(0, -1)
    print(*ans)


sol()