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
from collections import Counter
def primeFactorization(N):
    primes = Counter()
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
    isPrime = [True] * (N + 1)
    isPrime[0] = False
    isPrime[1] = False
    for i in range(2, N + 1):
        if not isPrime[i]:
            continue
        for p in range(i * 2, N, i):
            isPrime[p] = False
    return isPrime if isTable else [i for i in range(2, N) if isPrime[i]]

# 素因数分解(複数回)
class Prime:
    def __init__(self, N):
        smallestPrime = [1] * (N + 1)
        primes = []

        for i in range(2, N + 1):
            if smallestPrime[i] != 1:
                continue
            primes.append(i)
            for p in range(i * 2, N + 1, i):
                if smallestPrime[p] == 1:
                    smallestPrime[p] = i

        self.smallestPrime = smallestPrime
        self.primes = primes

    def isPrime(self, n):
        return n > 1 and self.smallestPrime[n] == 1

    def factorization(self, n):
        ret = Counter()
        while True:
            p = self.smallestPrime[n]
            if p == 1:
                break
            ret[p] += 1
            n //= p
        if n > 1:
            ret[n] += 1
        return ret