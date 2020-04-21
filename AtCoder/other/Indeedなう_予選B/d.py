N, C = map(int, input().split())
A = list(map(int, input().split()))

Is = [[0] for _ in range(C + 1)]
for i, a in enumerate(A, start=1):
    Is[a].append(i)
for i in range(C + 1):
    Is[i].append(N + 1)

for c in range(1, C + 1):
    I = Is[c]
    ans = N * (N + 1) // 2
    for l, r in zip(I, I[1:]):
        d = r - l - 1
        ans -= d * (d + 1) // 2
    print(ans)
