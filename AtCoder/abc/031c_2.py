N = int(input())
A = list(map(int, input().split()))

def calc(left, right):
    if left > right:
        left, right = right, left

    odd = 0
    even = 0
    for i, a in enumerate(A[left:right + 1], start=1):
        if i % 2 == 1:
            odd += a
        else:
            even += a
    return (odd, even)

def sol(taka):
    mxAoki = -10**18
    ret = None
    for i in range(N):
        if i == taka:
            continue
        odd, even = calc(i, taka)
        if mxAoki < even:
            ret = odd
            mxAoki = even

    return ret

ans = -10**18
for i in range(N):
    ans = max(ans, sol(i))
print(ans)
