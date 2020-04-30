N = int(input())
S = input()
T = input()
MOD = 10**9 + 7

isPrevI = S[0] == T[0]
i = 1 if isPrevI else 2
ans = 3 if isPrevI else 6

while i < N:
    if S[i] == T[i]:
        if isPrevI:
            ans *= 2
            ans %= MOD
        isPrevI = True
        i += 1
    else:
        if isPrevI:
            ans *= 2
            ans %= MOD
        else:
            ans *= 3
            ans %= MOD
        isPrevI = False
        i += 2

print(ans)
