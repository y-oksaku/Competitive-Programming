def sol():
    N, K = map(int, input().split())
    A = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append((a, b))

    def isOk(m):
        B = [w * (p - m) for w, p in A]
        if sum(sorted(B, reverse=True)[:K]) >= 0:
            return True
        else:
            return False

    left = 0
    right = 101
    while right - left > 1e-8:
        mid = (right + left) / 2
        if isOk(mid):
            left = mid
        else:
            right = mid

    print(left)

sol()

