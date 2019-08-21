N = int(input())

def primeFact(n) :
    primeList = {}
    for m in range(2, n + 1) :
        k = m
        for i in range(2, k + 1) :
            if k % i == 0 :
                if not i in primeList :
                    primeList[i] = 0
                while k % i == 0 :
                    primeList[i] += 1
                    k //= i
    return primeList

def dictFilter (filter, dic) :
    return { key : val for key, val in dic.items() if filter(key, val)}

primeN = primeFact(N)
prime75 = len(dictFilter(lambda key, val : val + 1 >= 75, primeN))
prime25 = len(dictFilter(lambda key, val : val + 1 >= 25, primeN))
prime15 = len(dictFilter(lambda key, val : val + 1 >= 15, primeN))
prime5 = len(dictFilter(lambda key, val : val + 1 >= 5, primeN))
prime3 = len(dictFilter(lambda key, val : val + 1 >= 3, primeN))

ans = 0
ans += prime75
ans += prime25 * (prime3 - 1)
ans += prime15 * (prime5 - 1)
ans += prime5 * (prime5 - 1) * (prime3 - 2) // 2

print(ans)
