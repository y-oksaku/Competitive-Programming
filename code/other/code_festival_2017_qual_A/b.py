N, M, K = map(int, input().split())

canMake = set()
for i in range(N + 1):
    for j in range(M + 1):
        area = (N - i) * (M - j) + i * j
        canMake.add(area)

if K in canMake:
    print('Yes')
else:
    print('No')