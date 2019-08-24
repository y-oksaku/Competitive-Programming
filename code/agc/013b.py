import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7

def sol():
    N, M = map(int, input().split())
    edges = [[] for _ in range(N)]

    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edges[a].append(b)
        edges[b].append(a)

    path = deque([0])
    visited = [False] * N
    visited[0] = True

    for _ in range(N - 1):
        for to in edges[path[-1]]:
            if not visited[to]:
                path.append(to)
                visited[to] = True
                break
        for leaf in edges[path[-1]]:
            if not visited[leaf]:
                break
        else:
            break

    for _ in range(N - 1):
        for to in edges[path[0]]:
            if not visited[to]:
                path.appendleft(to)
                visited[to] = True
                break
        for leaf in edges[path[0]]:
            if not visited[leaf]:
                break
        else:
            break

    print(len(path))
    ans = [p + 1 for p in path]
    print(*ans)


sol()