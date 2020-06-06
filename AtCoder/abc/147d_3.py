N = int(input())
A = list(map(int, input().split()))
MOD = 10**9 + 7

ans = 0
for d in range(60):
    mask = 1 << d
    Z = len([0 for a in A if (a & mask) == 0])
    ans += mask * Z * (N - Z)
    ans %= MOD
print(ans)
