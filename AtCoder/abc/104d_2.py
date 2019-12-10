S = input()
MOD = 10**9 + 7

A = 0
AB = 0
Q = 1
ans = 0

for s in S:
    if s == '?':
        ans = (3 * ans + AB) % MOD
        AB = (3 * AB + A) % MOD
        A = (3 * A + Q) % MOD
        Q = Q * 3 % MOD
    elif s == 'A':
        A = (A + Q) % MOD
    elif s == 'B':
        AB = (AB + A) % MOD
    elif s == 'C':
        ans = (ans + AB) % MOD

print(ans)
