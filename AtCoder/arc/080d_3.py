H, W = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))

ans = [[0] * W for _ in range(H)]
S = 0
for i, a in enumerate(A, start=1):
    for _ in range(a):
        h, w = divmod(S, W)
        ans[h][w] = i
        S += 1

for i, a in enumerate(ans):
    print(*a[::(-1)**i])
