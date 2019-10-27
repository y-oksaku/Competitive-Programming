import numpy as np

N = int(input())
A = np.array(input().split(), dtype=np.int32)
B = np.array(input().split(), dtype=np.int32)

ans = 0
pow = 1
for digit in range(30) :
    mask = pow*2 - 1
    maskedA = A & mask
    maskedB = B & mask

    maskedA.sort()
    maskedB.sort()

    sum1, sum2, sum3 = (np.searchsorted(maskedB, bound - maskedA).sum() for bound in [pow, pow*2, pow*3])
    count = sum1 + (sum3 - sum2)

    if (N - count) % 2 == 1 :
        ans += pow
    pow *= 2

print(ans)
