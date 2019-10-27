from collections import Counter

_, _ = map(int, input().split())
L = list(map(int, input().split()))
R = list(map(int, input().split()))

cntL = Counter(L)
cntR = Counter(R)

ans = 0
for l, cl in cntL.items():
    ans += min(cl, cntR[l])

print(ans)
