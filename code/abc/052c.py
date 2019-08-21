from collections import defaultdict

N = int(input())
MOD = 10**9 + 7

primeCount = defaultdict(int)

def primeList(n):
    p = 2
    primeList = defaultdict(int)
    while n > 1:
        if n % p == 0:
            while n % p == 0:
                primeList[p] += 1
                n //= p
        p += 1
    if n >= 2:
        primeList[n] = 1
    return primeList

for i in range(1, N + 1):
    for prime, count in primeList(i).items():
        primeCount[prime] += count

ans = 1
for _, count in primeCount.items():
    ans *= (count + 1)
    ans %= MOD

print(ans)