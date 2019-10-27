N = int(input())

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

primes = primeCount(N)

xor = 0
for cnt in primes.values():
    xor ^= cnt

if xor == 0:
    print('Bob')
else:
    print('Alice')