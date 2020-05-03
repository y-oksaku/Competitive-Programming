from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

cnt = defaultdict(int)
ans = 0
for i, a in enumerate(A, start=1):
    ans += cnt[-a + i]
    cnt[a + i] += 1

print(ans)
