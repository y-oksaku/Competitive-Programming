from bisect import bisect_left
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()

AB = defaultdict(int)

for b in B:
    AB[b] = bisect_left(A, b)

sumAB = defaultdict(int)
sumAB[0] = 0
s = 0
for b in B:
    s += AB[b]
    sumAB[b] = s

B.insert(0, 0)
ans = 0
for c in C:
    r = bisect_left(B, c)
    ans += sumAB[B[r - 1]]

print(ans)