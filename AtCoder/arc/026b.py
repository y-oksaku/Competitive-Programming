# 約数の全列挙
def divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

N = int(input())

div = divisors(N)

sumDiv = 0
for d in div:
    if d != N:
        sumDiv += d

if sumDiv == N:
    print('Perfect')
elif sumDiv < N:
    print('Deficient')
else:
    print('Abundant')