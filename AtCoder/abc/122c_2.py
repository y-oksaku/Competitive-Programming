N, Q = map(int, input().split())
S = input()

A = [0] * N
for i in range(1, N):
    if S[i - 1:i + 1] == 'AC':
        A[i] += 1

accA = [0] * (N + 1)
for i in range(1, N + 1):
    accA[i] = accA[i - 1] + A[i - 1]

for _ in range(Q):
    l, r = map(int, input().split())
    print(accA[r] - accA[l])
