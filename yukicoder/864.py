N = int(input())
K = int(input())

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

divK =  divisors(K)

ans = 0
for AB in divK:
    CD = K // AB
    if CD > 2 * N or AB > 2 * N:
        continue

    X = min(2 * N - (AB - 1), AB - 1)
    Y = min(2 * N - (CD - 1), CD - 1)
    ans += X * Y

print(ans)