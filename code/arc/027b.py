import string

class UnionFind :
    def __init__(self, size) :
        """
        Parameters
        ---
        size : int
            頂点数
        """
        self.parent = list(range(size))
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

        self.parent[root1] = min(root1, root2)
        self.parent[root2] = min(root1, root2)

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

N = int(input())
S1 = input()
S2 = input()

alphList = set()
alphToInt = {a : i for i, a in enumerate(string.ascii_uppercase)}
isConfilm = [False] * len(alphToInt)

tree = UnionFind(len(alphToInt))

for s1, s2 in zip(S1, S2):
    if (not s1.isdigit()) and (not s2.isdigit()):
        tree.union(alphToInt[s1], alphToInt[s2])
        alphList.add(s1)
        alphList.add(s2)

for s1, s2 in zip(S1, S2):
    if s1.isdigit() and s2.isdigit():
        continue
    if s1.isdigit():
        isConfilm[tree.root(alphToInt[s2])] = True
        alphList.add(s2)
    elif s2.isdigit():
        isConfilm[tree.root(alphToInt[s1])] = True
        alphList.add(s1)

ans = 1
for alph in alphList:
    if isConfilm[tree.root(alphToInt[alph])]:
        continue
    else:
        isConfilm[tree.root(alphToInt[alph])] = True
        if S1[0] == alph or S2[0] == alph:
            ans *= 9
        else:
            ans *= 10

print(ans)
