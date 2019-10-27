N = int(input())
A = [int(input()) for _ in range(N)]

A.sort()

if N % 2 == 0:
    small = A[:N // 2]
    big = A[N//2:]
    x = 2 * sum(small) - small[-1]
    y = 2 * sum(big) - big[0]
    ans = y - x
else:
    small = A[:N // 2]
    big = A[N // 2 + 1:]
    mid = A[N // 2]

    left = 2 * sum(big) - 2 * sum(small) - mid + small[-1]
    right = 2 * sum(big) - 2 * sum(small) + mid - big[0]

    ans = max(left, right)

print(ans)