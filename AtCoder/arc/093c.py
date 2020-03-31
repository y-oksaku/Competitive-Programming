N = int(input())
A = [0] + list(map(int, input().split())) + [0]

L = [0] * (N + 2)
for i in range(1, N + 2):
    L[i] = L[i - 1] + abs(A[i] - A[i - 1])

R = [0] * (N + 2)
for i in range(1, N + 2):
    R[i] = R[i - 1] + abs(A[N - i + 1] - A[N - (i - 1) + 1])

R = R[::-1]

ans = []
for i in range(1, N + 1):
    ans.append(L[i - 1] + R[i + 1] + abs(A[i - 1] - A[i + 1]))
print(*ans, sep='\n')