N, M = map(int, input().split())
S = input()
T = input()

# len(S) >= len(T) にする
if N < M:
    S, T = T, S
    N, M = M, N

for j, t in enumerate(T):
    if j * N % M == 0:
        k = j * N // M
        s = S[k]
        if t != s:
            print('-1')
            exit()

def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)

GCD = gcd(N, M)
LCM = N * M // GCD

print(LCM)

