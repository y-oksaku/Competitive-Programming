class UnionFind :
    """
    Union Find木
    ---
    頂点のインデックスは0~

    Attributes
    ---
    parent : list<int>
        親のリスト．parent[頂点のインデックス] = 親のインデックス
    height : list<int>
        各木の高さ
    size : list<int>
        各木の頂点数
    component : int
        連結成分の数
    """

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

tree = UnionFind(10)

def sol():
    N, M = map(int, input().split())

    edges = []
    for _ in range(M):
        fr, to, year = map(int, input().split())
        fr -= 1
        to -= 1
        edges.append((year, fr, to))

    Q = int(input())
    query = []
    for q in range(Q):
        country, year = map(int, input().split())
        country -= 1
        query.append((country, year, q))

    edges.sort(key=lambda A : A[0], reverse=True)
    query.sort(key=lambda A : A[1], reverse=True)

    ans = [0 for _ in range(Q)]
    tree = UnionFind(N)
    now = 0

    for country, year, q in query:
        while now < M and edges[now][0] > year:
            tree.union(edges[now][1], edges[now][2])
            now += 1
        ans[q] = tree.sizeOfSameRoot(country)

    print(*ans, sep='\n')

sol()