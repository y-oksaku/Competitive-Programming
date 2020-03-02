from collections import defaultdict
from itertools import product

_ = input()
N = list(map(int, input()))

cnt = [defaultdict(int) for _ in range(len(N) + 1)]
left = [10 ** 10] * 10
right = [-1] * 10

for i, n in enumerate(N):
    left[n] = min(left[n], i)
    right[n] = max(right[n], i)

    for j in range(10):
        cnt[i + 1][j] = cnt[i][j]
    cnt[i + 1][n] += 1

ans = 0
for l, m, r in product(range(10), repeat=3):
    l = left[l]
    r = right[r]

    if l < r and cnt[r][m] - cnt[l + 1][m] > 0:
        ans += 1

print(ans)
