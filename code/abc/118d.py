N , M = map(int,input().split())
A = list(map(int,input().split()))

A.sort(reverse=True)

match = [2,5,5,4,5,6,3,7,6]

dp = [-float('inf')] * (N + 1)

dp[0] = 0
for i in range(1, N+1) :
    maxDigit = -float('inf')
    for a in A :
        if i - match[a - 1] >= 0 :
            maxDigit = max(maxDigit, dp[i - match[a - 1]] + 1)
    dp[i] = maxDigit

maxDigit = dp[-1]

r = N

for _ in range(maxDigit) :
    for a in A :
        if r - match[a - 1] < 0 or r < 0 :
            continue
        if dp[r - match[a - 1]] == dp[r] - 1 :
            print(a, end='')
            r -= match[a - 1]
            break

print('')