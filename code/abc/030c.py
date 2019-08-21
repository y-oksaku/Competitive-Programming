N, M = map(int, input().split())
X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = 0
b = 0
time = -1
ans = 0

while a < N and b < M:
    while a < N and A[a] < time:
        a += 1

    if a >= N:
        break
    time = A[a] + X

    while b < M and B[b] < time:
        b += 1

    if b >= M:
        break
    time = B[b] + Y

    ans += 1

print(ans)