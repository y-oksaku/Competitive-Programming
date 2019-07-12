def factorial(n = 0) :
    ret = [1] * n
    for i in range(1,n) :
        ret[i] = ret[i-1] * i
    return ret

N = 10
fact = factorial(N)

def permutation(n,r) :
    return fact[n] // fact[n-r]

def combination(n,r) :
    return fact[n] // fact[n-r] // fact[r]

def ceil(a,b) :
    return (a + b - 1) // b

class Combination :
    def combi(self, n, k) :
        if n < k :
            return 1
        factK = 1
        factP = 1
        for i in range(1, k+1) :
            factK *= i
            factP *= n-i+1

        return factP // factK

    def permutation(self, n, k) :
        if n < k :
            return 1
        fact = 1
        for i in range(k) :
            fact *= n-i
        return fact

# MODにおける逆元
def modInv(a, MOD=1000000007) :
    b = MOD
    u = 1
    v = 0
    while b :
        t = a // b
        a -= t * b
        u -= t * v
        a, b = b, a
        u, v = v, u
    u = u % MOD
    return u

# 約数の全列挙
def divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    # divisors.sort(reverse=True)
    return divisors