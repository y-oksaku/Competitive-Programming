def sol():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]

    for mask in range(K**N):
        xor = 0
        for digit, t in enumerate(T):
            xor ^= t[(mask % (K**(digit + 1))) // (K**digit)]
        if xor == 0:
            print('Found')
            return
    print('Nothing')
    return

sol()
