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

import string

N = int(input())
S = input()
T = input()

A = [str(i) for i in range(10)] + list(string.ascii_uppercase)
I = {s: i for i, s in enumerate(A)}
tree = UnionFind(len(A))

for s, t in zip(S, T):
    tree.union(I[s], I[t])

def isNum(s):
    for i in range(10):
        if tree.isSameRoot(I[str(i)], I[s]):
            return True
    return False

V = set([tree.root(I[s]) for s in A if isNum(s)])
ans = 1
for i, s in enumerate(S):
    if tree.root(I[s]) in V:
        continue
    ans *= 9 if i == 0 else 10
    V.add(tree.root(I[s]))

print(ans)
