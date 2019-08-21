from bisect import bisect_right as bir

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

def isOk(v):
    count = 0
    for a in A:
        r = bir(B, v // a)
        count += r
        if count >= K:
            return True
    return False

right = A[-1] * B[-1] + 1
left = -1
while right - left > 1:
    middle = (left + right) // 2
    if isOk(middle):
        right = middle
    else:
        left = middle

print(right)