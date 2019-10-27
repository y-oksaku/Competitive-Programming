N, K = map(int, input().split())
A = list(map(int, input().split()))
sumA = sum(A)

# 約数の全列挙
def divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort(reverse = True)  # ソート
    return divisors

ansList = divisors(sumA)
ans = 1

for div in ansList :
    res = [a % div for a in A]
    res.sort(reverse=True)

    sumCount = sum(res)
    b = 0
    for r in res :
        sumCount -= r
        b += div - r
        if sumCount == b :
            if sumCount <= K :
                ans = div
                break
    else :
        continue
    break

print(ans)