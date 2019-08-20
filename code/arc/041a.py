def sol():
    X, Y = map(int, input().split())
    K = int(input())

    ans = min(Y, K)
    if K - ans > 0:
        ans += X - (K - ans)
    else:
        ans += X

    print(ans)

sol()