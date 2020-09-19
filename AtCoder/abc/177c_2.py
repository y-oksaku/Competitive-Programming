N = int(input())
A = list(map(int, input().split()))
MOD = 10**9 + 7

S = 0
ans = 0
for a in A:
    ans = (ans + a * S) % MOD
    S += a
print(ans)
