from collections import deque

class UnionFind :
    def __init__(self, size) :
        self.parent = list(range(size))
        self.height = [0] * size
        self.size = [1] * size
        self.component = size

    def root(self, index) :
        if self.parent[index] == index :  # 根の場合
            return index
        rootIndex = self.root(self.parent[index])  # 葉の場合親の根を取得
        self.parent[index] = rootIndex  # 親の付け直し
        return rootIndex

    def union(self, index1, index2) :  # 結合
        root1 = self.root(index1)
        root2 = self.root(index2)

        if root1 == root2 :  # 連結されている場合
            return

        self.component -= 1  # 連結成分を減らす

        if self.height[root1] < self.height[root2] :
            self.parent[root1] = root2  # root2に結合
            self.size[root2] += self.size[root1]
        else :
            self.parent[root2] = root1  # root1に結合
            self.size[root1] += self.size[root2]
            if self.height[root1] == self.height[root2] :
                self.height[root1] += 1
        return

    def isSameRoot(self, index1, index2) :
        return self.root(index1) == self.root(index2)

    def sizeOfSameRoot(self, index) :
        return self.size[self.root(index)]

    def getComponent(self) :
        return self.component

N, M = map(int, input().split())
tree = UnionFind(N)
edges = [[] for _ in range(N)]

for _ in range(M):
    p, q = map(int, input().split())
    p -= 1
    q -= 1
    tree.union(p, q)
    edges[p].append(q)
    edges[q].append(p)

def search(start):
    INF = float('inf')
    minDist = [INF] * N
    que = deque([(start, 0)])

    while que:
        now, dist = que.popleft()
        if minDist[now] <= dist:
            continue
        minDist[now] = dist
        for to in edges[now]:
            que.append((to, dist + 1))

    D = [d - 1 for d in minDist if 1 <= d and d != INF]
    if D:
        return max(D)
    else:
        return 0

# Qが十分小さい
Q = int(input())
ans = []
for _ in range(Q):
    A = int(input())
    A -= 1
    dist = search(A)
    day = dist.bit_length()
    ans.append((tree.sizeOfSameRoot(A) - 1, day))

for a, b in ans:
    print(a, b)