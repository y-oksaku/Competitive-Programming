from collections import deque
import sys
input = sys.stdin.buffer.readline

class LCA:
    def __init__(self, size, root):
        self.size = size
        self.root = root
        self.level = (size - 1).bit_length()
        self.edges = [[] for _ in range(size)]
        self.depth = [0] * size
        self.length = [0] * size
        self.prev = [None] * size
        self.kprev = None

    def addEdge(self, fr, to, cost=1):
        self.edges[fr].append((to, cost))
        self.edges[to].append((fr, cost))

    def dfs(self):
        st = deque([(self.root, self.root)])
        self.depth[self.root] = 0
        self.length[self.root] = 0
        while st:
            now, prev = st.pop()
            for to, cost in self.edges[now]:
                if to == prev:
                    continue
                st.append((to, now))
                self.depth[to] = self.depth[now] + 1
                self.length[to] = self.length[now] + cost
                self.prev[to] = now

    def construct(self):
        self.dfs()
        kprev = [self.prev]
        S = self.prev
        for _ in range(self.level):
            T = [0] * self.size
            for i in range(self.size):
                if S[i] is None:
                    continue
                T[i] = S[S[i]]
            kprev.append(T)
            S = T
        self.kprev = kprev

    def lca(self, u, v):
        dist = self.depth[v] - self.depth[u]
        if dist < 0:
            u, v = v, u
            dist = -dist

        for k in range(self.level + 1):
            if dist & 1:
                v = self.kprev[k][v]
            dist //= 2

        if u == v:
            return u

        for k in range(self.level)[:: -1]:
            prevU = self.kprev[k][u]
            prevV = self.kprev[k][v]
            if prevU != prevV:
                u = prevU
                v = prevV

        return self.kprev[0][u]

    def dist(self, u, v):
        return self.length[u] + self.length[v] - self.length[self.lca(u, v)] * 2

N = int(input())
root = -1
parent = [-1] * N

for ch in range(N):
    pr = int(input()) - 1
    if pr == -2:
        root = ch
    parent[ch] = pr

tree = LCA(N, root)
for ch in range(N):
    if ch == root:
        continue
    tree.addEdge(ch, parent[ch])
tree.construct()

Q = int(input())
ans = []
for _ in range(Q):
    ch, pr = map(lambda a: int(a) - 1, input().split())
    if tree.lca(ch, pr) == pr:
        ans.append('Yes')
    else:
        ans.append('No')
print(*ans, sep='\n')
