N, M = map(int, input().split())
grp = [[] for _ in range(N + 1)]

for i in range(M):
    P, Y = map(int, input().split())
    grp[P].append((Y, i))

ans = [''] * M
for P, YI in enumerate(grp[1:], start=1):
    YI.sort()
    for j, (_, i) in enumerate(YI):
        ans[i] = '%06d%06d' % (P, j + 1)

print(*ans, sep='\n')
