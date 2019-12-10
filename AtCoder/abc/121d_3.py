A, B = map(int, input().split())

# 1 ^ ... ^ n
# 0-1, 2-3, 4-5, ... でペアを作る
def g(n):
    one = (n + 1) // 2
    ret = one % 2

    if n % 2 == 0:
        ret ^= n

    return ret

ans = g(A - 1) ^ g(B)
print(ans)