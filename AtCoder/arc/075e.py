from bisect import bisect_right
import sys
input = sys.stdin.buffer.readline

class BIT:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def add(self, index):
        while index <= self.size:
            self.tree[index] += 1
            index += index & (-index)

    def sum(self, index):
        ret = 0
        while index:
            ret += self.tree[index]
            index -= index & (-index)
        return ret

    def search(self, value):
        i = 0
        s = 0
        step = 1 << (self.size.bit_length() - 1)
        while step:
            if i + step <= self.size and s + self.tree[i + step] < value:
                i += step
                s += self.tree[i]
            step //= 2
        return i + 1

N, K = map(int, input().split())
A = [int(input()) - K for _ in range(N)]

accA = [0] * (N + 1)
for i, a in enumerate(A, start=1):
    accA[i] = accA[i - 1] + a

sToI = {s: i for i, s in enumerate(sorted(list(set(accA))))}
tree = BIT(len(sToI))

ans = 0
for a in map(lambda a: sToI[a] + 1 ,accA):
    ans += tree.sum(a)
    tree.add(a)
print(ans)
