import math
N = int(input())
A = [int(input()) for _ in range(N)]
A.sort(reverse=True)

ans = 0
for i in range(N):
    ans += (-1)**i * A[i]**2

print(ans * math.pi)
