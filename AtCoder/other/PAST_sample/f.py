from collections import defaultdict

N = int(input())
S = [list(input()) for _ in range(N)]

cnt = defaultdict(int)
for s in S:
    s.sort()
    cnt[''.join(s)] += 1

ans = 0
for c in cnt.values():
    ans += c * (c - 1) // 2
print(ans)