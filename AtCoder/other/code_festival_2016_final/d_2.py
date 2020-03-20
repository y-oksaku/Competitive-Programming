from collections import Counter, defaultdict

N, M = map(int, input().split())
X = list(map(int, input().split()))

cntMod = defaultdict(int)
cntDup = defaultdict(int)

for x, c in Counter(X).items():
    cntMod[x % M] += c
    cntDup[x % M] += c // 2

ans = 0
for m in range(M):
    if m > M // 2:
        break
    n = (M - m) % M

    if n == m:
        ans += cntMod[n] // 2
    else:
        mi = min(cntMod[n], cntMod[m])
        ans += mi
        cntMod[n] -= mi
        cntMod[m] -= mi
        ans += min(cntMod[n] // 2, cntDup[n])
        ans += min(cntMod[m] // 2, cntDup[m])

print(ans)
