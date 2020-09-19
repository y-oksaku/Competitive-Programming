class BIT:
    """
    1-indexed
    """
    def __init__(self, size):
        self.size = size
        self.data = [0] * (size + 1)

    def add(self, index, value=1):
        while index <= self.size:
            self.data[index] += value
            index += index & (-index)

    def sum(self, index):
        """
        右端含める
        """
        ret = 0
        while index:
            ret += self.data[index]
            index -= index & (-index)
        return ret

    def search(self, val):
        """
        x_1 + ... x_i >= val を満たす最小のi
        """
        i = 0
        s = 0
        step = 1 << (self.size.bit_length() - 1)  # 一番上の長さ

        while step:
            if i + step <= self.size and s + self.data[i + step] < val:
                i += step
                s += self.data[i]
            step //= 2
        return i + 1

N = int(input())
A = list(map(int, input().split()))
aToI = {a: i for i, a in enumerate(A, start=1)}

tree = BIT(N)
for i in range(1, N + 1):
    tree.add(i)

ans = 0
for a in sorted(A):
    N -= 1
    l = tree.sum(aToI[a]) - 1
    r = N - l
    ans += min(l, r)
    tree.add(aToI[a], -1)

print(ans)
