import math
import fractions

# A以上B以下の数でXの倍数の個数
def countX(X) :
    if X > B :
        return 0

    minX = (A - 1) // X
    maxX = B // X

    return maxX - minX

A , B , C , D = map(int,input().split())

ans = B - A + 1

# 最小公倍数
Z = int(C * D / fractions.gcd(C,D))

ans -= countX(C)
ans -= countX(D)
ans += countX(Z)

print(int(ans))

