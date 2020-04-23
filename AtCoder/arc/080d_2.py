H, W = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))

ans = []
for i, a in enumerate(A, start=1):
    ans.extend([i] * a)
ans.sort()

for i, w in enumerate(range(0, H * W, W)):
    print(*ans[w: w + W][::(-1)**i])
