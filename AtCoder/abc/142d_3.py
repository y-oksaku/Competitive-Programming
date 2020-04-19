A, B = map(int, input().split())

def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)

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

G = gcd(A, B)
P = primeCount(G)

ans = 1 + len(P.keys())
print(ans)
