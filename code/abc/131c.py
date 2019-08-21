import math
import fractions

A , B , C , D = map(int,input().split())

# A以上B以下の数でXの倍数の個数
def countX(X) :
    if X > B :
        return 0
    minX = max(math.ceil(A / X),0)
    maxX = max(math.floor(B / X),0)
    return maxX - minX + 1

if C == 1 or D == 1 :
    print(0)
elif min(C,D) > B :
    print(A - B + 1)
elif max(C,D) % min(C,D) == 0 :
    Z = min(C,D)
    ans = B - A + 1 - countX(Z)
    print(ans + 1)
else :
    ans = B - A + 1

    # 最小公倍数
    Z = int(C * D / fractions.gcd(C,D))

    ans -= countX(C)
    ans -= countX(D)
    ans += countX(Z)

    print(ans)

