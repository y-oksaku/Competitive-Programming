N = int(input())
S = input()
T = input()
MOD = 10**9 + 7

isPrevI = S[0] == T[0]

ans = 3 if isPrevI else 6
now = 1 if isPrevI else 2

while now < N:
    isI = S[now] == T[now]

    if isPrevI:
        ans *= 2
    elif not isI:
        ans *= 3
    ans %= MOD
    now += 1 if isI else 2
    isPrevI = isI

print(ans)
