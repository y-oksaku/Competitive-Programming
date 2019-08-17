from itertools import product

def sol():
    N, _ = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]

    for values in product(*T):
        xor = 0
        for v in values:
            xor ^= v
        if xor == 0:
            print('Found')
            return
    print('Nothing')
    return

sol()
