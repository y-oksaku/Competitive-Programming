from collections import defaultdict

cnt = defaultdict(int)

N = int(input())
for _ in range(N):
    cnt[input()] += 1

M = int(input())
for _ in range(M):
    cnt[input()] -= 1

ans = 0
for c in cnt.values():
    ans = max(ans, c)
print(ans)
