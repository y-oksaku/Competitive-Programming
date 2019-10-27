N, K = map(int, input().split())

numbers = [tuple(map(int, input().split())) for _ in range(N)]

# bitwise-orがK以下になるには
# ある桁kが存在し，K & (1 << k) == 1 and n & (1 << k) == 0 かつ上位kビットのみでK以下

def isOk(k, n):
    maskK = (K >> k)
    maskN = (n >> k)

    if maskN % 2 == 1:
        return False

    if (maskK | maskN) == maskK:
        return True
    else:
        return False

ans = sum([a for n, a in numbers if (n | K) == K])
for k in range(30):
    if K & (1 << k):
        s = 0
        for n, a in numbers:
            if isOk(k, n):
                s += a
        ans = max(ans, s)

print(ans)
