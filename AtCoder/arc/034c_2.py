from collections import Counter
A, B = map(int, input().split())

# 素数のリスト
def createPrimeList(N, isTable=True):
    isPrime = [True] * N
    isPrime[0] = False
    isPrime[1] = False
    for i in range(2, N):
        if not isPrime[i]:
            continue
        for p in range(i * 2, N, i):
            isPrime[p] = False
    return isPrime if isTable else [i for i in range(2, N) if isPrime[i]]

# 素因数分解(複数回)
isPrime = createPrimeList(int(A**0.5) + 100, False)
def primeFactorization(N):
    primes = Counter()
    for p in isPrime:
        while N % p == 0:
            N //= p
            primes[p] += 1
    if N > 1:
        primes[N] += 1
    return primes

primes = Counter()
for i in range(B + 1, A + 1):
    primes += primeFactorization(i)

ans = 1
MOD = 10**9 + 7
for c in primes.values():
    ans = (ans * (c + 1)) % MOD
print(ans)
