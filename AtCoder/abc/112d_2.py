N, M = map(int, input().split())

# 約数の全列挙
def divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort(reverse=True)  # ソート
    return divisors

for k in divisors(M):
    if k * N <= M:
        print(k)
        exit()