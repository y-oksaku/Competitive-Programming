from functools import lru_cache
import sys
sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())

parent = [[] for _ in range(N)]
child = [[] for _ in range(N)]

for _ in range(N - 1 + M):
    pr, ch = map(int, input().split())
    pr -= 1
    ch -= 1
    parent[ch].append(pr)
    child[pr].append(ch)

root = parent.index([])
ans = [-1] * N

# 葉からの検索を行う
@lru_cache(maxsize=None)
def search(now):
    if now == root:
        ans[now] = 0
        return 0
    ret = -1
    for pr in parent[now]:
        depth = search(pr)
        if depth > ret:
            ans[now] = pr + 1
            ret = depth
    return ret + 1

for i in range(N):
    search(i)

print(*ans, sep='\n')