A, R, N = map(int, input().split())

M = A
if R > 1:
    while M <= 10**9 and N > 1:
        M *= R
        N -= 1

print('large' if M > 10**9 else M)
