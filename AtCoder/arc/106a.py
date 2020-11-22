N = int(input())

for B in range(1, N):
    if pow(5, B) > N:
        break
    M = N - pow(5, B)

    A = 0
    while M > 0 and M % 3 == 0:
        M //= 3
        A += 1

    if M == 1 and A > 0 and B > 0:
        print(A, B)
        exit()

print(-1)
