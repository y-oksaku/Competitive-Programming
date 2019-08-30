import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7
INF = float('inf')

class Dinic:
    def __init__(self, size):
        self.size = size
        self.edges = [[] for _ in range(size)]
        self.depth = None
        self.progress = None

    def addEdge(self, fr, to, cap):
        self.edges[fr].append([cap, to, len(self.edges[to])])
        self.edges[to].append([0, fr, len(self.edges[fr]) - 1])

    def bfs(self, s):
        depth = [-1] * self.size
        depth[s] = 0
        que = deque([s])

        while que:
            now = que.popleft()
            for cap, to, _ in self.edges[now]:
                if cap > 0 and depth[to] < 0:
                    depth[to] = depth[now] + 1
                    que.append(to)
        self.depth = depth

    def dfs(self, s, t, flow):
        if s == t:
            return flow

        for i, (cap, to, rev) in enumerate(self.edges[s][self.progress[s]:], start=self.progress[s]):
            self.progress[s] = i
            if cap == 0 or self.depth[s] >= self.depth[to]:
                continue
            d = self.dfs(to, t, min(flow, cap))
            if d == 0:
                continue
            self.edges[s][i][0] -= d
            self.edges[to][rev][0] += d
            return d
        return 0

    def maxFlow(self, s, t):
        flow = 0
        while True:
            self.bfs(s)
            if self.depth[t] < 0:
                return flow
            self.progress = [0] * self.size
            currentFlow = self.dfs(s, t, float('inf'))
            while currentFlow > 0:
                flow += currentFlow
                currentFlow = self.dfs(s, t, float('inf'))

def sol():
    N, _, E = map(int, input().split())
    P = list(map(int, input().split()))
    A = []
    edges = [[] for _ in range(N)]

    for _ in range(E):
        fr, to = map(int, input().split())
        A.append((fr, to))
        edges[fr].append(to)
        edges[to].append(fr)

    depth = [-1] * (N + 1)
    st = deque([0])
    depth[0] = 0
    while st:
        now = st.popleft()
        for to in edges[now]:
            if depth[to] == -1:
                depth[to] = depth[now] + 1
                st.append(to)

    flow = Dinic(N + 1)
    for fr, to in A:
        if depth[fr] > depth[to]:
            fr, to = to, fr
        flow.addEdge(fr, to, 1)

    for p in P:
        flow.addEdge(p, N, 1)

    print(flow.maxFlow(0, N))

sol()