from heapq import heappop, heappush

class MinCostFlow:
    def __init__(self, size):
        self.size = size
        self.edges = [[] for _ in range(size)]

    def addEdge(self, fr, to, cap, cost):
        self.edges[fr].append([to, cap, cost, len(self.edges[to])])
        self.edges[to].append([fr, 0, -cost, len(self.edges[fr]) - 1])

    def minCostFlow(self, s, t, f):
        N = self.size
        edges = self.edges
        INF = 10**18

        res = 0
        H = [0] * N
        prevV = [0] * N
        prevE = [0] * N

        while f:
            dist = [INF] * N
            dist[s] = 0

            que = [(0, s)]

            while que:
                c, now = heappop(que)
                if dist[now] < c:
                    continue

                for i, (to, cap, cost, _) in enumerate(edges[now]):
                    if cap > 0 and dist[to] > dist[now] + cost + H[now] - H[to]:
                        r = dist[now] + cost + H[now] - H[to]
                        dist[to] = r
                        prevV[to] = now
                        prevE[to] = i
                        heappush(que, (r, to))

            if dist[t] == INF:
                return -INF

            for i, d in enumerate(dist):
                H[i] += d

            d = f
            now = t
            while now != s:
                d = min(d, edges[prevV[now]][prevE[now]][1])
                now = prevV[now]

            f -= d
            res += d * H[t]
            now = t
            while now != s:
                edge = edges[prevV[now]][prevE[now]]
                edge[1] -= d
                edges[now][edge[3]][1] += d
                now = prevV[now]
        return res