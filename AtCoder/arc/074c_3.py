H, W = map(int, input().split())

if H % 3 == 0 or W % 3 == 0:
    print(0)
    exit()

ans = min(H, W)
for A, B in ((H, W), (W, H)):
    for a in (A // 3, A // 3 + 1):
        for b in (B // 2, B // 2 + 1):
            X = a * B
            Y = (A - a) * b
            Z = (A - a) * (B - b)

            ans = min(ans, max(X, Y, Z) - min(X, Y, Z))
print(ans)
