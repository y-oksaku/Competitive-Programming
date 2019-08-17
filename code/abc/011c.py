def sol():
    N = int(input())
    NG = [int(input()) for _ in range(3)]

    if N in NG:
        print('NO')
        return

    for _ in range(100):
        if not N - 3 in NG:
            N -= 3
            continue
        if not N - 2 in NG:
            N -= 2
            continue
        if not N - 1 in NG:
            N -= 1
            continue

    if N <= 0:
        print('YES')
    else:
        print('NO')

sol()