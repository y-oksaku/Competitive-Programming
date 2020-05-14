from collections import defaultdict

N = int(input())

cnt = defaultdict(int)
for i in range(1, N + 1):
    i = str(i)
    l = i[0]
    r = i[-1]
    cnt[(l, r)] += 1
    cnt[(r, l)] += 0

ans = 0
for (l, r), c in cnt.items():
    ans += cnt[(r, l)] * c

print(ans)
