from collections import defaultdict
from bisect import bisect_right

S = input()
T = input()
N = len(S)

setS = set(S)
for t in set(T):
    if t not in setS:
        print(-1)
        exit()

sToI = defaultdict(list)
for i, s in enumerate(S):
    sToI[s].append(i)
for s in set(S):
    sToI[s].append(float('inf'))

cnt = 0
last = -1
now = -1
for t in T:
    i = bisect_right(sToI[t], now)
    to = sToI[t][i]
    if to == float('inf'):
        cnt += 1
        now = sToI[t][0]
    else:
        now = to
    last = now
print(cnt * N + last + 1)