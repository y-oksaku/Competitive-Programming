from collections import defaultdict
from bisect import bisect_right

def sol():
    S = input()
    T = input()

    setS = set(S)
    setT = set(T)
    for t in setT:
        if not t in setS:
            print('-1')
            return

    posS = defaultdict(list)

    for i, s in enumerate(S):
        posS[s].append(i)

    for s in enumerate(S):
        posS[s].sort()

    prev = -1
    ans = 0
    N = len(S)

    for t in T:
        next = bisect_right(posS[t], prev)
        if next >= len(posS[t]):
            ans += N - prev
            ans += posS[t][0]
            prev = posS[t][0]
        else:
            ans += posS[t][next] - prev
            prev = posS[t][next]

    print(ans)

sol()
