# 階乗
def factorial(n = 0) :
    ret = [1] * n
    for i in range(1,n) :
        ret[i] = ret[i-1] * i
    return ret

N = 10
fact = factorial(N)

# 前計算を用いた組み合わせ計算
def permutation(n,r) :
    return fact[n] // fact[n-r]

def combination(n,r) :
    return fact[n] // fact[n-r] // fact[r]

def ceil(a,b) :
    return (a + b - 1) // b

# 組み合わせ計算
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
