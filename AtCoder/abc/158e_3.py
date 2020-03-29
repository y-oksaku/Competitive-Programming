N, P = map(int, input().split())
S = input()

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

def largeSol():
    cnt = [0] * P
    cnt[0] += 1
    ret = 0
    now = 0
    for i, s in enumerate(map(int, S[:: -1])):
        now = (pow(10, i, P) * s + now) % P
        ret += cnt[now - P]
        cnt[now] += 1
    return ret

print(smallSol() if N * P <= 10**6 else largeSol())
