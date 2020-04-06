from collections import Counter
N = int(input())
A = Counter(map(int, input().split()))

S = []
for a, c in A.items():
    S.extend([a] * (c // 2))

S.sort()
if len(S) < 2:
    print(0)
else:
    print(S[-1] * S[-2])
