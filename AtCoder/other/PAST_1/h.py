INF = 10**18

class MinSegTree:
    """
    0-indexed
    query : [L, R)
    """
    def __init__(self, size):
        self.size = 1 << (size.bit_length())  # 完全二分木にする
        self.data = [INF] * (2 * self.size - 1)

    def build(self, rawData):
        self.data[self.size - 1: self.size - 1 + len(rawData)] = rawData
        for i in range(self.size - 1)[:: -1]:
            self.data[i] = min(self.data[2 * i + 1], self.data[2 * i + 2])

    def update(self, index, value):
        index += self.size - 1
        self.data[index] = value
        while index >= 0:
            index = (index - 1) // 2
            self.data[index] = min(self.data[2 * index + 1], self.data[2 * index + 2])

    def query(self, left, right):
        L = left + self.size
        R = right + self.size
        ret = INF
        while L < R:
            if R & 1:
                R -= 1
                ret = min(ret, self.data[R - 1])
            if L & 1:
                ret = min(ret, self.data[L - 1])
                L += 1
            L >>= 1
            R >>= 1
        return ret

N = int(input())
C = [INF] + list(map(int, input().split()))
O = C[1::2]
E = C[::2]

oddTree = MinSegTree(len(O))
oddTree.build(O)
evenTree = MinSegTree(len(E))
evenTree.build(E)

Q = int(input())
ans = 0
even = 0
odd = 0

for _ in range(Q):
    query = tuple(map(int, input().split()))

    if query[0] == 1:
        _, x, a = query
        D = even if x % 2 == 0 else odd

        if C[x] - D >= a:
            ans += a
            C[x] -= a
            if x % 2 == 0:
                evenTree.update(x // 2 - 1, C[x])
            else:
                oddTree.update(x // 2, C[x])
    if query[0] == 2:
        a = query[1]
        if oddTree.query(0, len(O)) - odd >= a:
            ans += a * len(O)
            odd += a
    if query[0] == 3:
        a = query[1]
        if min(oddTree.query(0, len(O)) - odd, evenTree.query(0, len(E)) - even) >= a:
            ans += a * N
            odd += a
            even += a

print(ans)
