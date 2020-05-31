N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]
A = [a for a, _ in AB]
B = [b for _, b in AB]
A.sort()
B.sort()

if N % 2 == 1:
    mi = A[N // 2]
    mx = B[N // 2]
    print(mx - mi + 1)
else:
    mi = A[N // 2] + A[N // 2 - 1]
    mx = B[N // 2] + B[N // 2 - 1]
    print(mx - mi + 1)
