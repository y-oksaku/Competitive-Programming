def sol():
    N = int(input())
    A = list(map(int, input().split()))

    prod = 1
    for a in A:
        prod *= a

    b = 0
    for a in A:
        b += prod // a

    ans = prod / b
    print(ans)

sol()