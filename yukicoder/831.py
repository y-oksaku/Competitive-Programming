N = int(input())

if N == 1:
    print(0)
elif N % 2 == 0:
    print((N**3 + 3 * N**2 + 5 * N - 6) // 6)
else:
    print((N**3 + 3 * N**2 + 5 * N - 3) // 6)