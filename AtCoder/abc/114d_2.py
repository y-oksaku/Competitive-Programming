from collections import defaultdict

N = int(input())

def getPrimes(N):
    R = N + 10
    isPrime = [True] * (R + 2)
    primes = set()

    for p in range(2, R):
        if not isPrime[p]:
            continue
        primes.add(p)
        for q in range(p * 2, R, p):
            isPrime[q] = False

    return primes

primes = getPrimes(N)

def getFactors(N):
    facts = defaultdict(int)
    for p in primes:
        while N % p == 0:
            facts[p] += 1
            N //= p
    return facts

fracFacts = defaultdict(int)
for i in range(1, N + 1):
    for p, c in getFactors(i).items():
        fracFacts[p] += c

cnt = {
    2 : 0,
    4 : 0,
    14 : 0,
    24 : 0,
    74 : 0,
}

for c in fracFacts.values():
    for k in cnt.keys():
        if c >= k:
            cnt[k] += 1

ans = 0
ans += cnt[4] * (cnt[4] - 1) * (cnt[2] - 2) // 2
ans += cnt[14] * (cnt[4] - 1)
ans += cnt[24] * (cnt[2] - 1)
ans += cnt[74]
print(ans)