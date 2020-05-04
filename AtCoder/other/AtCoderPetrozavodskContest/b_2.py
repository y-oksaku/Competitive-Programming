N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

K = sum(B) - sum(A)

cntA = 0
for i in range(N):
    a, b = A[i], B[i]
    d = b - a
    if d > 0:
        d = -(-d // 2)
        cntA += d
        A[i] += d * 2

cntB = 0
for i in range(N):
    a, b = A[i], B[i]
    d = a - b
    if d > 0:
        cntB += d
        B[i] += d

if max(cntA, cntB) > K:
    print('No')
    exit()

dA = K - cntA
dB = K - cntB

print('Yes' if dA * 2 == dB else 'No')