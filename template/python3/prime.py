# 約数の全列挙
def divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    # divisors.sort(reverse=True)  # ソート
    return divisors

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

