N = int(input())
A = list(map(int, input().split()))
M = sum(A)

if M % N != 0:
    print(-1)
    exit()

ans = 0
now = 0
left = 0
K = M // N

while left < N:
    now = A[left]
    right = left + 1
    while right < N and now != (right - left) * K:
        now += A[right]
        right += 1
        ans += 1
    left = right

print(ans)