N = int(input())
A = list(map(int, input().split()))
A.sort()

if A[0] < 0 and A[-1] > 0:
    ans = 0
    for a in A:
        ans += abs(a)
    print(ans)
    now = A[0]
    for a in A[1:N - 1]:
        if a >= 0:
            print(now, a)
            now -= a
    print(A[-1], now)
    now = A[-1] - now
    for a in A[1: -1]:
        if a < 0:
            print(now, a)
            now -= a
elif A[0] >= 0:
    ans = sum(A) - A[0] * 2
    print(ans)
    now = A[0]
    for a in A[1: -1]:
        print(now, a)
        now -= a
    print(A[-1], now)
else:
    ans = -sum(A) + A[-1] * 2
    print(ans)
    now = A[-1]
    for a in A[: -1]:
        print(now, a)
        now -= a