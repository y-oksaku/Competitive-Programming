from heapq import heappush, heappop
from collections import defaultdict

N = int(input())

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

primes = primeFactorization(N).keys()

que = []
for p in primes:
    heappush(que, (p, p))

ans = 0
while que and N > 0:
    z, p = heappop(que)
    if N % z == 0:
        ans += 1
        N //= z

        heappush(que, (z * p, p))

print(ans)
