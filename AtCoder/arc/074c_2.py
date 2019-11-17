H, W = map(int, input().split())

if H % 3 == 0 or W % 3 == 0:
    print(0)
    exit()

ans = min(H, W)
for w1 in [W // 3, W // 3 + 1]:
    w23 = W - w1
    for h2 in [H // 2, H // 2 + 1]:
        h3 = H - h2

        S1 = w1 * H
        S2 = h2 * w23
        S3 = h3 * w23

        ans = min(ans, max(S1, S2, S3) - min(S1, S2, S3))

for h1 in [H // 3, H // 3 + 1]:
    h23 = H - h1
    for w2 in [W // 2, W // 2 + 1]:
        w3 = W - w2

        S1 = h1 * W
        S2 = w2 * h23
        S3 = w3 * h23

        ans = min(ans, max(S1, S2, S3) - min(S1, S2, S3))

print(ans)