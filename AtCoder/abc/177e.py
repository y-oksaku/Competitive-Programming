from math import gcd

N = int(input())
A = list(map(int, input().split()))

def isSetwise(A):
    ret = A[0]
    for a in A:
        ret = gcd(ret, a)
    return ret == 1
from collections import Counter

def createPrimeList(N):
    isPrime = [True] * (N + 1)
    isPrime[0] = False
    isPrime[1] = False
    smallestPrime = [1] * (N + 1)
    for i in range(2, N + 1):
        if not isPrime[i]:
            continue
        for p in range(i * 2, N, i):
            if isPrime[p]:
                smallestPrime[p] = i
            isPrime[p] = False
    return smallestPrime

from collections import Counter
smallestPrime = createPrimeList(max(A) + 10)
def primeFactorization(N):
    ret = Counter()
    while N > 1:
        p = smallestPrime[N]
        if p == 1:
            ret[N] += 1
            break
        ret[p] += 1
        N //= p
    return ret

def isPairwise(A):
    P = Counter()
    for a in A:
        for p in primeFactorization(a):
            if P[p] >= 1:
                return False
            P[p] += 1
    return True

if not isSetwise(A):
    print('not coprime')
    exit()

if isPairwise(A):
    print('pairwise coprime')
else:
    print('setwise coprime')
