N = int(input())
A = list(map(int, input().split()))

right = 0
left = 0
sumEx = 0
sumNo = 0
ans = 0

while left < N :
    while right < N :
        if (sumEx ^ A[right]) == (sumNo + A[right]) :
            sumEx += A[right]
            sumNo += A[right]
            right += 1
            continue
        break
    ans += right - left
    sumEx ^= A[left]
    sumNo -= A[left]
    left += 1

print(ans)