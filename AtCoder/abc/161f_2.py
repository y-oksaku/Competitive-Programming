N = int(input())

def isOk(k):
    n = N
    while n % k == 0:
        n //= k
    return n % k == 1

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

divN = divisors(N)
divN1 = divisors(N - 1)

ans = len([0 for d in divN if d > 1 and isOk(d)]) + len([0 for d in divN1 if d > 1 and isOk(d)])

print(ans)
