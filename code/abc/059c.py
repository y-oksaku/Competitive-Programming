N = int(input())
A = list(map(int, input().split()))

pos = 0
left = A[0]
if left <= 0:
    pos += 1 - left
    left = 1
for a in A[1:]:
    if left * (left + a) < 0:
        left += a
    else:
        if left + a == 0:
            if left < 0:
                left += a + 1
            else:
                left += a - 1
            pos += 1
        else:
            pos += abs(left + a) + 1
            if left < 0:
                left = 1
            else:
                left = -1

neg = 0
left = A[0]
if left >= 0:
    neg += left + 1
    left = -1
for a in A[1:]:
    if left * (left + a) < 0:
        left += a
    else:
        if left + a == 0:
            if left < 0:
                left += a + 1
            else:
                left += a - 1
            neg += 1
        else:
            neg += abs(left + a) + 1
            if left < 0:
                left = 1
            else:
                left = -1

print(min(neg, pos))