def getPrimes(n):
    isPrime = [True] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if isPrime[i]:
            primes.append(i)
        for p in primes:
            if i * p > n:
                break
            isPrime[i * p] = False
            if i % p == 0:
                break
    return primes

N = 5000000
input()
A = set(input().split())
prev = set()

ans = -1
left = 1
for p in getPrimes(N):
    V = set(str(p))
    if len(V - A) > 0:
        if len(prev) == len(A):
            ans = max(ans, p - 1 - left)
        prev = set()
        left = p + 1
    else:
        prev |= V

if len(prev) == len(A):
    ans = max(ans, N - left)

print(ans)
