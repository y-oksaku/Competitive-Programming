H, W = map(int, input().split())
M = (H + W) * 80

A = [tuple(map(int, input().split())) for _ in range(H)]
B = [tuple(map(int, input().split())) for _ in range(H)]

dp = [[0] * W for _ in range(H)]
dp[0][0] = (1 << (M - abs(A[0][0] - B[0][0])))

for h in range(H):
    for w, (a, b) in enumerate(zip(A[h], B[h])):
        d = abs(a - b)
        mask = 0
        if h > 0:
            mask |= (dp[h - 1][w] << d)
            mask |= (dp[h - 1][w] >> d)
        if w > 0:
            mask |= (dp[h][w - 1] << d)
            mask |= (dp[h][w - 1] >> d)
        dp[h][w] |= mask

state = dp[-1][-1]
nums = []
for digit, b in enumerate(bin(state)[2:][:: -1]):
    if b == '1':
        nums.append(digit - M)
ans = min(abs(n) for n in nums)
print(ans)
