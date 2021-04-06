from collections import defaultdict
import sys
input = sys.stdin.readline

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.height = [0] * size
        self.size = [1] * size
        self.componentCount = size

    def root(self, index):
        if self.parent[index] == index:  # 根の場合
            return index
        rootIndex = self.root(self.parent[index])  # 葉の場合親の根を取得
        self.parent[index] = rootIndex  # 親の付け直し
        return rootIndex

    def union(self, index1, index2):  # 結合
        root1 = self.root(index1)
        root2 = self.root(index2)

        if root1 == root2:  # 連結されている場合
            return

        self.componentCount -= 1  # 連結成分を減らす

        if self.height[root1] < self.height[root2]:
            self.parent[root1] = root2  # root2に結合
            self.size[root2] += self.size[root1]
        else:
            self.parent[root2] = root1  # root1に結合
            self.size[root1] += self.size[root2]
            if self.height[root1] == self.height[root2]:
                self.height[root1] += 1
        return

    def isSameRoot(self, index1, index2):
        return self.root(index1) == self.root(index2)

    def sizeOfSameRoot(self, index):
        return self.size[self.root(index)]

N, Q = map(int, input().split())
C = list(map(int, input().split()))
QAB = [tuple(map(int, input().split())) for _ in range(Q)]

tree = UnionFind(N)
cnt = [defaultdict(int) for _ in range(N)]
for i, c in enumerate(C):
    cnt[i][c - 1] = 1

for q, a, b in QAB:
    a -= 1
    b -= 1

    if q == 1:
        ra, rb = tree.root(a), tree.root(b)
        if ra == rb:
            continue
        tree.union(a, b)
        rc = tree.root(a)

        if ra != rc:
            ra, rb = rb, ra
        for key, value in cnt[rb].items():
            cnt[ra][key] += value
    else:
        print(cnt[tree.root(a)][b])
