from collections import Counter
N = int(input())
V = list(map(int, input().split()))

A = V[::2]
B = V[1::2]

cntA = list(Counter(A).items())
cntB = list(Counter(B).items())

cntA.sort(key=lambda a: a[1], reverse=True)
cntB.sort(key=lambda a: a[1], reverse=True)

ans = 10**18
for a, c in cntA[:2]:
    for b, d in cntB[:2]:
        if a != b:
            ans = min(ans, N - c - d)
        elif max(len(cntA), len(cntB)) == 1:
                ans = min(ans, min(len(A), len(B)))

print(ans)
