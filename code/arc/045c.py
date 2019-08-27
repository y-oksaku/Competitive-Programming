import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7
INF = float('inf')

def sol():
    N, X = map(int, input().split())
    edges = [[] for _ in range(N)]

    for _ in range(N - 1):
        fr, to, cost = map(int, input().split())
        fr -= 1
        to -= 1
        edges[fr].append((to, cost))
        edges[to].append((fr, cost))

    minDist = [-1] * N
    st = deque([(0, 0)])

    distList = defaultdict(int)

    while st:
        now, dist = st.pop()

        minDist[now] = dist
        distList[dist] += 1

        for to, cost in edges[now]:
            if minDist[to] == -1:
                st.append((to, dist ^ cost))

    if X > 0:
        ans = 0
        for dist, count in distList.items():
            if dist ^ X in distList:
                ans += count * distList[dist ^ X]

        print(ans // 2)
    else:
        ans = 0
        for _, count in distList.items():
            ans += count * (count - 1) // 2
        print(ans)

sol()