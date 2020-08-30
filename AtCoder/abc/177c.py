N = int(input())
A = list(map(int, input().split()))
MOD = 10**9 + 7
S = sum(A)

ans = 0
for a in A:
    S = (S - a) % MOD
    ans += S * a
    ans %= MOD
print(ans)
