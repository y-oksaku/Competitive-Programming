from collections import deque

class Combination:
    def __init__(self, size, mod=10**9 + 7):
        self.size = size + 2
        self.mod = mod
        self.fact = [1, 1] + [0] * size
        self.inv = [0, 1] + [0] * size

        for i in range(2, self.size):
            self.fact[i] = self.fact[i - 1] * i % self.mod
            self.inv[i] = -self.inv[self.mod % i] * (self.mod // i) % self.mod

N = int(input())
MOD = 10**9 + 7
edges = [[] for _ in range(N)]

for _ in range(N - 1):
    fr, to = map(int, input().split())
    fr -= 1
    to -= 1
    edges[fr].append(to)
    edges[to].append(fr)

depth = [-1] * N

st = deque([(0, -1, 0)])
while st:
    now, pr, d = st.pop()
    depth[now] = d
    for to in edges[now]:
        if to == pr:
            continue
        st.append((to, now, d + 1))

comb = Combination(N + 10)
ans = 0
facN = comb.fact[N]
inv = comb.inv
for i in range(N):
    ans += facN * inv[depth[i] + 1]
    ans %= MOD

print(ans)