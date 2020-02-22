from collections import defaultdict
N = int(input())
cnt = defaultdict(int)

for _ in range(N):
    cnt[input()] += 1

mx = max(cnt.values())
cnt = [s for s, n in cnt.items() if n == mx]
cnt.sort()

print(*cnt, sep='\n')
