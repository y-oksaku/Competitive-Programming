from collections import Counter

N = int(input())
T = [int(input()) for _ in range(N)]
MOD = 10**9 + 7

T.sort()

ans = 0
now = 0

for t in T:
    now += t
    ans += now

fact = [1] * (N + 1)
for i in range(1, N + 1):
    fact[i] = (fact[i - 1] * i) % MOD

cntT = Counter(T)
cnt = 1
for c in cntT.values():
    cnt *= fact[c]
    cnt %= MOD

print(ans)
print(cnt)