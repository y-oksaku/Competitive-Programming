from collections import deque

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

    def factN(self, n):
        if n < 0:
            return 0
        return self.fact[n]

N, K = map(int, input().split())
MOD = 10**9 + 7
edges = [[] for _ in range(N)]

for _ in range(N - 1):
    fr, to = map(int, input().split())
    fr -= 1
    to -= 1
    edges[fr].append(to)
    edges[to].append(fr)

comb = Combination(N + K + 100)

chCnt = [0] * N
que = deque([(0, -1)])
while que:
    now, pr = que.popleft()
    chCnt[now] = len(edges[now]) - 1
    for to in edges[now]:
        if to != pr:
            que.append((to, now))
chCnt[0] += 1

ans = K
que = deque([(0, -1)])
while que:
    now, pr = que.popleft()

    if pr == -1:
        ans *= comb.npr(K - 1, chCnt[now])
    else:
        ans *= comb.npr(K - 2, chCnt[now])

    ans %= MOD
    for to in edges[now]:
        if to != pr:
            que.append((to, now))

print(ans % MOD)
