from bisect import bisect_left, bisect_right

R, C, K = map(int, input().split())
N = int(input())

rowCount = [0 for _ in range(R)]
columnCount = [0 for _ in range(C)]
seed = []

for _ in range(N):
    r, c = map(int, input().split())
    rowCount[r - 1] += 1
    columnCount[c - 1] += 1
    seed.append((r - 1, c - 1))

ans = 0
for r, c in seed:
    if rowCount[r] + columnCount[c] == K:
        ans -= 1
    if rowCount[r] + columnCount[c] - 1 == K:
        ans += 1

columnCount.sort()

for r in rowCount:
    ans += bisect_right(columnCount, K - r) - bisect_left(columnCount, K - r)

print(ans)