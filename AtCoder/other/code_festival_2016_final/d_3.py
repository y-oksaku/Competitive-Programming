from collections import Counter
N, M = map(int, input().split())
cntX = Counter(map(int, input().split()))

cntMod = Counter()
cntDup = Counter()
for x, c in cntX.items():
    cntMod[x % M] += c
    cntDup[x % M] += c // 2

ans = 0
for n in range(M // 2 + 1):
    m = (M - n) % M
    if m == n:
        ans += cntMod[n] // 2
        continue

    cnt = min(cntMod[n], cntMod[m])
    cntMod[n] -= cnt
    cntMod[m] -= cnt

    ans += cnt
    ans += min(cntMod[n] // 2, cntDup[n]) + min(cntMod[m] // 2, cntDup[m])
print(ans)
