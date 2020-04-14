N = int(input())
A = list(map(int, input().split()))
MOD = 10**9 + 7

ans = 0
for d in range(62):
    mask = (1 << d)
    zero = len([0 for a in A if (a & mask) == 0])
    ans += zero * (N - zero) * mask % MOD
print(ans % MOD)
