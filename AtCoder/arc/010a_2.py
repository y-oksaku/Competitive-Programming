
def sol():
    N, M, A, B = map(int, input().split())

    for d in range(1, M + 1):
        if N <= A:
            N += B
        c = int(input())

        if N < c:
            print(d)
            return
        N -= c

    print('complete')
    return

sol()
