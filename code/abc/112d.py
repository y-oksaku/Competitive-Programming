N, M = map(int, input().split())

def divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort(reverse=True)
    return divisors

div = divisors(M)

for d in div :
    if M >= N * d :
        print(d)
        break


