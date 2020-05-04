from collections import defaultdict

N, M = map(int, input().split())

A = defaultdict(list)
for i in range(M):
    P, Y = map(int, input().split())
    A[P].append((Y, i))

ans = [''] * M
for p, grp in A.items():
    for j, (_, i) in enumerate(sorted(grp), start=1):
        ans[i] = '%06d%06d' % (p, j)
print(*ans, sep='\n')

