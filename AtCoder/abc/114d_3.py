from collections import Counter
N = int(input())

def getPrimes():
    isPrime = [True] * 100
    primes = []
    for p in range(2, 100):
        if not isPrime[p]:
            continue
        primes.append(p)
        for i in range(p, 100, p):
            isPrime[i] = False
    return primes

P = getPrimes()
A = Counter()

for n in range(1, N + 1):
    cnt = Counter()
    for p in P:
        while n % p == 0:
            n //= p
            cnt[p] += 1
    A += cnt

D = {3: 0, 5: 0, 15: 0, 25: 0, 75: 0}
for k in D.keys():
    for c in A.values():
        if (c + 1) >= k:
            D[k] += 1

ans = 0
ans += (D[5] * (D[5] - 1) // 2) * (D[3] - 2)
ans += D[15] * (D[5] - 1)
ans += D[25] * (D[3] - 1)
ans += D[75]
print(ans)
