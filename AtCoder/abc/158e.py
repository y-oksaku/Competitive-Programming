from collections import Counter
N, P = map(int, input().split())
S = input()

def largeSol():
    T = [0] * (N + 1)
    for i, s in enumerate(map(int, S[:: -1])):
        T[i + 1] = (s * pow(10, i, P) + T[i]) % P

    ans = 0
    cnt = Counter(T[1:])
    for p in range(P):
        x = cnt[p]
        ans += x * (x - 1) // 2
    ans += cnt[0]
    return ans

def smallSol():
    dp = [0] * P
    ans = 0
    for s in map(int, S):
        newDp = [0] * P
        newDp[s % P] += 1
        for p in range(P):
            newDp[(p * 10 + s) % P] += dp[p]
        dp = newDp
        ans += dp[0]
    return ans

print(smallSol() if N * P <= 10**7 else largeSol())
