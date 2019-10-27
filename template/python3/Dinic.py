from collections import deque

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

