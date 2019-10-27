def sol():
    N = int(input())
    for i in range(1, 10):
        for j in range(1, 10):
            N -= i * j

    N = abs(N)
    ans = set()
    for i in range(1, 10):
        if N % i == 0:
            if 1 <= i <= 9 and 1 <= N // i <= 9:
                ans.add((i, N // i))

    ans = list(ans)
    ans.sort()

    for i, j in ans:
        print('{} x {}'.format(i, j))

sol()