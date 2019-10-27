K = int(input())
N = int(input())

def primes(n):
    primeList = set()
    isPrime = [True] * (n + 1)
    for i in range(2, n + 1):
        if isPrime[i]:
            primeList.add(i)
            k = i * 2
            while k <= n:
                isPrime[k] = False
                k += i

    return primeList

primeK = primes(K - 1)
primeN = primes(N)
rangePrimes = list(primeN - primeK)
rangePrimes.sort()

def f(n):
    while sum(map(int, str(n))) >= 10:
        n = sum(map(int, str(n)))
    return sum(map(int, str(n)))

hashPrimes = [f(p) for p in rangePrimes]

maxLeng = 0
V = set()
M = len(hashPrimes)
ans = -1
right = 0

for left in range(M):
    while right < M and (not hashPrimes[right] in V):
        V.add(hashPrimes[right])
        right += 1

    if maxLeng <= len(V):
        maxLeng = len(V)
        ans = left

    V.remove(hashPrimes[left])

print(rangePrimes[ans])
