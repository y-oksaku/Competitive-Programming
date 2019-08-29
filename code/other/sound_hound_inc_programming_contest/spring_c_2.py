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

def index(C, r, c):
    return r * C + c + 2

def sol():
    R, C = map(int, input().split())
    chart = [input().rstrip() for _ in range(R)]

    count = sum([s.count('.') for s in chart])

    flow = Dinic(R * C + 2)
    s = 0
    t = 1

    for r in range(R):
        for c in range(C):
            if chart[r][c] == '*' or (r + c) % 2 == 1:
                continue
            if r < R - 1 and chart[r + 1][c] == '.':
                flow.addEdge(index(C, r, c), index(C, r + 1, c), 1)
            if r > 0 and chart[r - 1][c] == '.':
                flow.addEdge(index(C, r, c), index(C, r - 1, c), 1)
            if c < C - 1 and chart[r][c + 1] == '.':
                flow.addEdge(index(C, r, c), index(C, r, c + 1), 1)
            if c > 0 and chart[r][c - 1] == '.':
                flow.addEdge(index(C, r, c), index(C, r, c - 1), 1)

    for r in range(R):
        for c in range(C):
            if chart[r][c] == '.':
                if (r + c) % 2 == 0:
                    flow.addEdge(s, index(C, r, c), 1)
                else:
                    flow.addEdge(index(C, r, c), t, 1)

    print(count - flow.maxFlow(s, t))

sol()