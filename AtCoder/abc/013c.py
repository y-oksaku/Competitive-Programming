def sol():
    N, H = map(int, input().split())
    A, B, C, D, E = map(int, input().split())

    ans = float('inf')

    for x in range(N + 1):
        now = H + x * B
        res = E * (N - x)

        if now - res > 0:
            ans = min(ans, x * A)
        else:
            y = ((res - now) // (E + D)) + 1
            ans = min(ans, x * A + y * C)

    print(ans)

sol()