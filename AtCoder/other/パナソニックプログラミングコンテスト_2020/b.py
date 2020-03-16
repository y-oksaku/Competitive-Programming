H, W = map(int, input().split())

if min(H, W) == 1:
    print(1)
    exit()

ans = W * (H // 2)

if H % 2 == 1:
    ans += -(-W // 2)

print(ans)
