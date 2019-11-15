L = input()
MOD = 10**9 + 7
now = 1
ans = 1
for b in L[:: -1]:
    if b == '1':
        ans = (ans * 2 + now) % MOD
    else:
        ans = ans % MOD
    now = now * 3 % MOD
print(ans % MOD)