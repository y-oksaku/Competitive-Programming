N = int(input())
A = list(map(int, input().split()))

S = sum(A)
if S % (N * (N + 1) // 2) != 0:
    print('NO')
    exit()

K = S // (N * (N + 1) // 2)
B = [r - l - K for r, l in zip(A[1:] + [A[0]], A)]

if not all(b <= 0 and b % N == 0 for b in B):
    print('NO')
    exit()

if K == -sum([b // N for b in B]):
    print('YES')
    exit()

print('NO')
