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
    posCount = 0
    negCount = 0
    middleCount = 0

    for a in A :
        b = a % div  # 倍数までの距離
        if b < (div - b) :
            negCount += b
        elif b > (div - b) :
            posCount += (div - b)
        else :
            middleCount += b

    if (posCount + negCount + middleCount) <= 2 * K :
        if (posCount - negCount - middleCount) % 2 == 0 :
            ans = div
            break

print(ans)