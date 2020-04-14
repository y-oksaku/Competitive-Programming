Q = int(input())
R = 10**5 + 100

def getPrimes():
    isPrime = [True] * R
    isPrime[0] = False
    isPrime[1] = False
    for i in range(R):
        if not isPrime[i]:
            continue
        for p in range(i * 2, R, i):
            isPrime[p] = False
    return isPrime

isPrime = getPrimes()
A = [1 if i % 2 == 1 and isPrime[i] and isPrime[(i + 1) // 2] else 0 for i in range(R)]
accA = [0] * R
for i in range(1, R):
    accA[i] = accA[i - 1] + A[i - 1]
accA = accA[1:]

for _ in range(Q):
    l, r = map(int, input().split())
    print(accA[r] - accA[l - 1])

