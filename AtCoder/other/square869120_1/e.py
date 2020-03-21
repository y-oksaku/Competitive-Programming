N, Q = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(lambda a: int(a) - 1, input().split()))
MOD = 10**9 + 7

D = [pow(a, b, MOD) for a, b in zip(A, A[1:])]
accD = [0] * N

for i in range(1, N):
    accD[i] = (accD[i - 1] + D[i - 1]) % MOD

ans = 0
for fr, to in zip([0] + C, C + [0]):
    if fr > to:
        fr, to = to, fr
    ans += accD[to] - accD[fr]
    ans %= MOD

print(ans)
