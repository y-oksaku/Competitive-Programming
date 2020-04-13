
Q = int(input())
N = 10**5 + 1000

def getPrimes():
    isPrime = [True] * N
    isPrime[1] = False
    for i in range(2, N):
        if not isPrime[i]:
            continue
        for p in range(i + i, N, i):
            isPrime[p] = False
    return isPrime

isPrime = getPrimes()

A = [0] * (N)
for i in range(2, N):
    if i % 2 == 1 and isPrime[i] and isPrime[(i + 1) // 2]:
        A[i] = 1
accA = [0] * (N + 1)
for i, a in enumerate(A, start=0):
    accA[i] += accA[i - 1] + a

for _ in range(Q):
    l, r = map(int, input().split())
    print(accA[r] - accA[l - 1])

