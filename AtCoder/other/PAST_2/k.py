import sys
sys.setrecursionlimit(10**7)

N, Q = map(int, input().split())

parent = [-1] * (N + 1)
top = list(range(N + 1))

for _ in range(Q):
    fr, to, x = map(int, input().split())

    px = parent[x]
    parent[x] = top[to]
    top[to] = top[fr]
    top[fr] = px

ans = [-1] * (N + 1)

def search(now, root):
    if now == -1 or ans[now] != -1:
        return
    ans[now] = root
    return search(parent[now], root)

for i in range(1, N + 1):
    search(top[i], i)

print(*ans[1:], sep='\n')
