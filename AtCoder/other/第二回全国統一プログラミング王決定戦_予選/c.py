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

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for a, b in zip(sorted(A), sorted(B)):
    if a > b:
        print('No')
        exit()

# Bの昇順でAを並び替え
BA = list(zip(A, B))
BA.sort()

AI = [(a, i) for i, (_, a) in enumerate(BA)]
AI.sort()

tree = UnionFind(N)
for nessIndex, (_, originalIndex) in enumerate(AI):
    tree.union(nessIndex, originalIndex)

V = set()
for i in range(N):
    V.add(tree.root(i))

if len(V) > 1:  # サイクルが複数の場合
    print('Yes')
    exit()

if any(a <= b for a, b in zip(sorted(A)[1:], sorted(B)[:-1])):
    print('Yes')
    exit()

print('No')