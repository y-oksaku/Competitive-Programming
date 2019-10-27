from collections import defaultdict

N, D, T = map(int, input().split())
X = list(map(int, input().split()))

amebaGrp = defaultdict(list)
for x in X:
    amebaGrp[x % D].append(x)

ans = N
for grp in amebaGrp.values():
    if not grp:
        continue

    grp.sort()
    ans += 2 * T

    for i in range(1, len(grp)):
        cnt = (grp[i] - grp[i - 1]) // D - 1
        ans += min(2 * T, cnt)

print(ans)
