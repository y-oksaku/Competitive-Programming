from itertools import combinations
from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
cnt = defaultdict(int)
for _ in range(N):
    s = input()
    cnt[s[0]] += 1

ans = 0
for h in combinations(['M', 'A', 'R', 'C', 'H'], r=3):
    prd = 1
    for s in h:
        prd *= cnt[s]
    ans += prd
print(ans)
