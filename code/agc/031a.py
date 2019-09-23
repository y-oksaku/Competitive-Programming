from collections import Counter

N = int(input())
S = input()
MOD = 10**9 + 7

cntS = Counter(S)

ans = 1
for c in cntS.values():
    ans *= (c + 1)
    ans %= MOD

print((ans - 1) % MOD)