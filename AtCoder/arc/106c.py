N, M = map(int, input().split())

if N == 1 and M == 0:
    print(1, 2)
    exit()

if M < 0 or N - 2 < M:
    print(-1)
    exit()

print(1, 10**8)
L = 2
for _ in range(M + 1):
    print(L, L + 1)
    L += 2
N -= M + 2

L = 10**8 + 1
for _ in range(N):
    print(L, L + 1)
    L += 2
