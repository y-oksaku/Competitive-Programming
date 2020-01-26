N = int(input())
A = list(map(int, input().split()))

ans = 0

xor = A[0]
now = A[0]
right = 1
for left in range(N):
    while right < N and xor ^ A[right] == now + A[right]:
        xor ^= A[right]
        now += A[right]
        right += 1
    ans += right - left
    now -= A[left]
    xor ^= A[left]

print(ans)