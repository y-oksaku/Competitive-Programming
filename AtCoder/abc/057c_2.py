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

ans = len(str(N))
for a in divisors(N):
    b = N // a
    ans = min(ans, max(len(str(a)), len(str(b))))
print(ans)