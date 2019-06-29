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
