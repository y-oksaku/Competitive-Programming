# 約数の全列挙
def divisors(n):
    divisors = []
    R = int(n**(0.5)) + 1
    for i in range(1, R):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    # divisors.sort(reverse=True)  # ソート
    return divisors

# 素因数分解(1回のみ)
from collections import defaultdict
def primeFactorization(N):
    primes = defaultdict(int)
    R = int(N**(0.5)) + 1
    for num in range(2, R):
        while N % num == 0:
            N //= num
            primes[num] += 1
    if N > 1 :
        primes[N] = 1
    return primes

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
from collections import defaultdict
isPrime = createPrimeList(10**5, False)
def primeFactorization2(N):
    primes = defaultdict(int)
    for p in isPrime:
        while N % p == 0:
            N //= p
            primes[p] += 1
    return primes
