class MaxSegTree:
    """
    0-indexed
    query : [L, R)
    """
    def __init__(self, size):
        self.size = 1 << (size.bit_length())  # 完全二分木にする
        self.data = [-INF] * (2 * self.size - 1)

    def build(self, rawData):
        self.data[self.size - 1: self.size - 1 + len(rawData)] = rawData
        for i in range(self.size - 1)[:: -1]:
            self.data[i] = max(self.data[2 * i + 1], self.data[2 * i + 2])

    def update(self, index, value):
        index += self.size - 1
        self.data[index] = value
        while index >= 0:
            index = (index - 1) // 2
            self.data[index] = max(self.data[2 * index + 1], self.data[2 * index + 2])

    def query(self, left, right):
        L = left + self.size
        R = right + self.size
        ret = -INF
        while L < R:
            if R & 1:
                R -= 1
                ret = max(ret, self.data[R - 1])
            if L & 1:
                ret = max(ret, self.data[L - 1])
                L += 1
            L >>= 1
            R >>= 1
        return ret

N = int(input())
H = [int(input()) for _ in range(N)]
INF = 10**18

tree = MaxSegTree(N)
for i, h in enumerate(H):
    tree.update(i, h)

def searchL(i):
    if i == 0:
        return 0
    h = H[i]
    ok = i
    ng = -1
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if tree.query(mid, i) <= h:
            ok = mid
        else:
            ng = mid
    return i - ok

def searchR(i):
    if i == N - 1:
        return 0

    h = H[i]
    ok = i
    ng = N
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if tree.query(i, mid + 1) <= h:
            ok = mid
        else:
            ng = mid
    return ok - i

ans = []
for i in range(N):
    ans.append(searchL(i) + searchR(i))

print(*ans, sep='\n')
