from itertools import accumulate
from bisect import bisect_right

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

accA = list(accumulate(A, initial=0))
accB = list(accumulate(B, initial=0))

ans = 0
for c, a in enumerate(accA):
    if K - a < 0:
        continue
    ans = max(ans, c + bisect_right(accB, K - a) - 1)
print(ans)
