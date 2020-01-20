from collections import defaultdict
from bisect import bisect_left

N = int(input())
WH = [tuple(map(int, input().split())) for _ in range(N)]
A = defaultdict(list)

for w, h in WH:
    A[w].append(h)

dp = [10**10]
for w in range(10**5 + 10):
    for h in sorted(A[w], reverse=True):
        i = bisect_left(dp, h)
        if i == len(dp):
            dp.append(h)
        else:
            dp[i] = min(dp[i], h)

print(len(dp))
