N = int(input())

def isOk(k):
    n = N
    while n % k == 0:
        n //= k
    return n % k == 1

if N <= 10**6:
    ans = 0
    for i in range(2, N + 1):
        if isOk(i):
            ans += 1
    print(ans)
    exit()

ans = 0
V = set()
for i in range(2, int(N**0.5) + 10):
    if isOk(i):
        ans += 1
        V.add(i)

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

divN = divisors(N - 1)

ans += len([d for d in divN if not d in V])
print(ans)
