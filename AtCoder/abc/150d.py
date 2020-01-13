N, M = map(int, input().split())
A = list(map(int, input().split()))

def gcd(m, n):
    if n == 0:
        return m
    return gcd(n, m % n)

LCM = A[0]
for a in A:
    LCM = LCM * a // gcd(LCM, a)

step = max(A)
X = step // 2
while X <= M:
    for a in A:
        if (X - a // 2) % a != 0:
            break
    else:
        cnt = X // LCM + (M - X) // LCM + 1
        print(cnt)
        exit()
    X += step
print(0)