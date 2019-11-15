L = input()
N = len(L)
MOD = 10**9 + 7

dpAll = [0] * (N + 1)
dpLess = [0] * (N + 1)

dpAll[0] = 1
dpLess[0] = 1

for d, b in enumerate(L[:: -1], start=1):
    dpAll[d] = dpAll[d - 1] * 3
    if b == '1':
        dpLess[d] = dpLess[d - 1] * 2 + dpAll[d - 1]
    else:
        dpLess[d] = dpLess[d - 1]
    dpAll[d] %= MOD
    dpLess[d] %= MOD

print(dpLess[N] % MOD)