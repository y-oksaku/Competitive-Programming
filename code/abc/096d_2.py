N = int(input())

def makePrimes():
    primeList = []
    isPrime = [True for _ in range(55556)]
    isPrime[0] = False
    isPrime[1] = False

    for i in range(2, 55556):
        if not isPrime[i]:
            continue
        if i % 5 == 1:
            primeList.append(i)

        for j in range(i, 55556, i):
            isPrime[j] = False

    return primeList

primeList = makePrimes()
print(*primeList[:N])