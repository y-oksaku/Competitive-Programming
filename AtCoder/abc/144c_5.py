N = int(input())

# 約数の全列挙
def divisors(n):
    divisors = []
    R = int(n**(0.5)) + 1
    for i in range(1, R):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    # divisors.sort(reverse=True)  # ソート
    return divisors

ans = 10**18
for d in divisors(N):
    k = N // d

    ans = min(ans, d + k - 2)
print(ans)
