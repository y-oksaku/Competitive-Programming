import sys
input = sys.stdin.buffer.readline

class Combination:
    def __init__(self, size, mod=10**9 + 7):
        self.size = size + 2
        self.mod = mod
        self.fact = [1, 1] + [0] * size
        self.factInv = [1, 1] + [0] * size
        self.inv = [0, 1] + [0] * size

        for i in range(2, self.size):
            self.fact[i] = self.fact[i - 1] * i % self.mod
            self.inv[i] = -self.inv[self.mod % i] * (self.mod // i) % self.mod
            self.factInv[i] = self.factInv[i - 1] * self.inv[i] % self.mod

    def npr(self, n, r):
        if n < r or n < 0 or r < 0:
            return 0
        return self.fact[n] * self.factInv[n - r] % self.mod

    def ncr(self, n, r):
        if n < r or n < 0 or r < 0:
            return 0
        return self.fact[n] * (self.factInv[r] * self.factInv[n - r] % self.mod) % self.mod

    def nhr(self, n, r):  # 重複組合せ
        return self.ncr(n + r - 1, n - 1)

    def factN(self, n):
        if n < 0:
            return 0
        return self.fact[n]

    def factInvN(self, n):
        if n < 0:
            return 0
        return self.factInv[n]

N = int(input())
MOD = 10**9 + 7
comb = Combination(N + 100)

edges = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    fr, to = map(int, input().split())
    edges[fr].append(to)
    edges[to].append(fr)

order = []
parent = [0] * (N + 1)
st = [1]
while st:
    now = st.pop()
    order.append(now)
    for to in edges[now]:
        if to == parent[now]:
            continue
        st.append(to)
        parent[to] = now

size = [1] * (N + 1)
for v in order[::-1]:
    size[parent[v]] += size[v]

dpLeaf = [1] * (N + 1)
for v in order[:: -1]:
    pr = parent[v]
    dpLeaf[v] = dpLeaf[v] * comb.fact[size[v] - 1] % MOD
    dpLeaf[pr] = dpLeaf[pr] * dpLeaf[v] * comb.factInv[size[v]] % MOD

ans = [0] * (N + 1)
ans[1] = dpLeaf[1]
for v in order[1:]:
    pr = parent[v]
    ans[v] = ans[pr] * comb.inv[N - size[v]] * size[v] % MOD

print(*(ans[1:]), sep='\n')