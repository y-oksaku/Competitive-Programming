N, P = map(int, input().split())
A = list(map(int, input().split()))

class Combination:
    def __init__(self, size):
        self.size = size
        self.fact = [1] * size
        for i in range(1, size):
            self.fact[i] = i * self.fact[i - 1]

    def ncr(self, n, r):
        if r > n or n < 0 or r < 0:
            return 0
        return self.fact[n] // self.fact[r] // self.fact[n - r]

odd = 0
even = 0
for a in A:
    if a % 2 == 0:
        even += 1
    else:
        odd += 1

ans = 0
comb = Combination(N + 100)
if P == 0:  # oddを偶数個
    for o in range(0, odd + 1, 2):
        for e in range(even + 1):
            ans += comb.ncr(odd, o) * comb.ncr(even, e)
else:
    for o in range(1, odd + 1, 2):
        for e in range(even + 1):
            ans += comb.ncr(odd, o) * comb.ncr(even, e)

print(ans)