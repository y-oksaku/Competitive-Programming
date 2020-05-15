from collections import Counter

N, M = map(int, input().split())
X = list(map(int, input().split()))

dupCnt = Counter()
modCnt = Counter()

for x, c in Counter(X).items():
    x %= M
    dupCnt[x] += c // 2
    modCnt[x] += c

ans = 0
for i in range(M):
    j = M - i
    if i > j:
        break
    if i == j or i == 0:
        ans += modCnt[i] // 2
        continue

    mi = min(modCnt[i], modCnt[j])
    ans += mi

    ans += min((modCnt[i] - mi) // 2, dupCnt[i])
    ans += min((modCnt[j] - mi) // 2, dupCnt[j])

print(ans)
