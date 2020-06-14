from collections import Counter
N = int(input())
A = list(map(int, input().split()))
cntA = Counter(A)

A.sort()
V = set()

ans = 0
mx = max(A)
for a in A:
    if a in V:
        continue
    if cntA[a] == 1:
        ans += 1

    p = a
    while p <= mx:
        V.add(p)
        p += a

print(ans)
