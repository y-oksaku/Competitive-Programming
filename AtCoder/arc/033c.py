class SegmentTree:
    """
    0-indexed
    query : [L, R)
    """
    def __init__(self, size, initValue, cmpFunc):
        self.size = 1 << (size.bit_length())  # 完全二分木にする
        self.data = [initValue] * (2 * self.size - 1)
        self.initValue = initValue
        self.cmpFunc = cmpFunc

    def build(self, rawData):
        self.data[self.size - 1: self.size - 1 + len(rawData)] = rawData
        for i in range(self.size - 1)[:: -1]:
            self.data[i] = self.cmpFunc(self.data[2 * i + 1], self.data[2 * i + 2])

    def update(self, index, value):
        index += self.size - 1
        self.data[index] = value
        while index >= 0:
            index = (index - 1) // 2
            self.data[index] = self.cmpFunc(self.data[2 * index + 1], self.data[2 * index + 2])

    def query(self, left, right):
        L = left + self.size
        R = right + self.size
        ret = self.initValue
        while L < R:
            if R & 1:
                R -= 1
                ret = self.cmpFunc(ret, self.data[R - 1])
            if L & 1:
                ret = self.cmpFunc(ret, self.data[L - 1])
                L += 1
            L >>= 1
            R >>= 1
        return ret

Q = int(input())
N = 210000
tree = SegmentTree(N, 0, lambda a, b: a + b)

ans = []
for _ in range(Q):
    T, X = map(int, input().split())
    if T == 1:
        tree.update(X, 1)
    else:
        ng = 0
        ok = N
        while ok - ng > 1:
            mid = (ok + ng) // 2
            if tree.query(0, mid) < X:
                ng = mid
            else:
                ok = mid
        ans.append(ok - 1)
        tree.update(ok - 1, 0)

for a in ans:
    print(a)