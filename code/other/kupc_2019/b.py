class UnionFind :
    def __init__(self, size) :
        """
        Parameters
        ---
        size : int
            頂点数
        """
        self.parent = list(range(size))
        self.height = [0] * size
        self.size = [1] * size
        self.component = size

    def root(self, index) :
        """
        親のインデックスの取得

        Parameters
        ---
        index : int
            取得する頂点のインデックス

        Returns
        ---
        rootIndex : int
            指定した頂点の根のインデックス
        """
        if self.parent[index] == index :  # 根の場合
            return index
        rootIndex = self.root(self.parent[index])  # 葉の場合親の根を取得
        self.parent[index] = rootIndex  # 親の付け直し
        return rootIndex

    def union(self, index1, index2) :  # 結合
        """
        木の結合

        Parameters
        ---
        index1 : int
        index2 : int
            結合する頂点のインデックス
        """
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
        """
        同じ木に属するかを判定する

        Parameters
        ---
        index1 : int
        index2 : int

        Returns
        ---
        boolean
        """
        return self.root(index1) == self.root(index2)

    def sizeOfSameRoot(self, index) :
        """
        指定した頂点の属する木の大きさを取得する
        """
        return self.size[self.root(index)]

    def getComponent(self) :
        """
        連結成分数を取得する
        """
        return self.component

from collections import defaultdict

N, M, W = map(int, input().split())
items = []

for _ in range(N):
    w, v = map(int, input().split())
    items.append((w, v))

tree = UnionFind(N)

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    tree.union(a, b)

compItem = defaultdict(lambda : [0, 0])
for i, (w, v) in enumerate(items):
    compItem[tree.root(i)][0] += w
    compItem[tree.root(i)][1] += v

dp = [[0] * (W + 1) for _ in range(len(compItem.keys()) + 1)]

for i, (w, v) in enumerate(compItem.values()):
    for weight in range(W + 1):
        dp[i + 1][weight] = max(dp[i + 1][weight], dp[i][weight])
        if weight + w <= W:
            dp[i + 1][weight + w] = max(dp[i + 1][weight + w], dp[i][weight] + v)

print(dp[len(compItem.keys())][W])