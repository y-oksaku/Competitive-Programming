N = int(input())
A = list(map(int, input().split()))

class BIT :
    def __init__(self, size) :
        self.bit = [0] * (size + 1)
        self.size = size

    def add(self, index, value) :
        while index <= self.size :
            self.bit[index] += value
            index += index & (-index)

    def sum(self, index) :
        ret = 0
        while index > 0 :
            ret += self.bit[index]
            index -= index & (-index)
        return ret

count = [0] * N
for i, a in enumerate(A) :
    S = [0]
    for j in range(N) :
        add = 1 if A[j] > a else -1
        S.append(S[-1] + add)

    minS = abs(min(S)) + 1 if min(S) <= 0 else 0
    maxS = max(S) + minS
    bit = BIT(2**(maxS.bit_length() + 1))

    for index, s in enumerate(S) :
        bit.add(s + minS, 1)
        count[i] += bit.sum(s + minS)

print(count)