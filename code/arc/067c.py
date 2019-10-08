from collections import defaultdict

N = int(input())
MOD = 10**9 + 7

def primeCount(N):
    R = int(N**(0.5)) + 1  # 素数の範囲
    primes = {}  # 素数のリスト
    n = N
    for num in range(2, R):
        primes[num] = 0
        while n % num == 0:
            n //= num
            primes[num] += 1
    if n > 1 :
        primes[n] = 1
    return { key : val for key, val in primes.items() if val > 0}  # フィルターをかける

primes = defaultdict(int)
for i in range(1, N + 1):
    ps = primeCount(i)
    for p, c in ps.items():
        primes[p] += c

ans = 1
for c in primes.values():
    ans *= (c + 1)
    ans %= MOD

print(ans % MOD)