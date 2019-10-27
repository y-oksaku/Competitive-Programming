from functools import lru_cache

N = int(input())

class Combination:
    def __init__(self, n):
        self.n = n
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i
        self.fact = fact

    def ncr(self, n, r):
        if n < 0 or r < 0 or n < r:
            return 0
        return self.fact[n] // self.fact[n - r] // self.fact[r]

comb = Combination(N + 10)

def prob(n, k):  # n人→k人の確率
    if n == k:
        ret = 0
        if n % 3 == 0:
            ret += q(n // 3, n // 3, n // 3)
        ret += q(n, 0, 0) * 3
        return ret
    ret = 0
    for G in range(n + 1):
        for C in range(n + 1):
            P = n - G - C
            if P < 0:
                break
            g, c, p = sorted([G, C, P])

            if g == c == 0 or g == c == p:
                continue
            elif g == 0:
                if c == k:
                    ret += q(g, c, p)
            elif g == k:
                ret += q(g, c, p)

    return ret

@lru_cache(maxsize=None)
def q(g, c, p):
    n = g + c + p
    return comb.ncr(n, g) * comb.ncr(n - g, c) / pow(3, n)

@lru_cache(maxsize=None)
def search(n):
    if n == 1:
        return 0
    ret = 0
    for i in range(1, n):
        ret += prob(n, i) * (search(i) + 1)
    ret += prob(n, n)
    return ret / (1 - prob(n, n))

ans = search(N)
print(ans)


