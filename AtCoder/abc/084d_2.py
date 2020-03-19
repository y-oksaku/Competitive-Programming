Q = int(input())
R = 10**5 + 10

def getPrimes():
    isPrime = [True] * R
    ret = []
    for i in range(2, R):
        if not isPrime[i]:
            continue
        ret.append(i)
        for j in range(i, R, i):
            isPrime[j] = False
    return set(ret)

P = getPrimes()

def isOk(n):
    return n in P and (n + 1) // 2 in P

A = [0] * R
for i in range(R):
    if isOk(i):
        A[i] += 1

for i in range(1, R):
    A[i] += A[i - 1]

ans = []
for _ in range(Q):
    l, r = map(int, input().split())
    ans.append(A[r] - A[l - 1])

print(*ans, sep='\n')