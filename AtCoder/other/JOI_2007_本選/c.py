from itertools import product
from bisect import bisect_right
import sys
input = sys.stdin.buffer.readline

N, M = map(int, input().split())
P = [int(input()) for _ in range(N)] + [0]

Q = [a + b for a, b in product(P, repeat=2) if a + b <= M]
Q.sort()
Q += [10**10]

ans = 0
for a in Q:
    b = a + Q[bisect_right(Q, M - a) - 1]
    if ans < b <= M:
        ans = b

print(ans)
